import csv
import os
import sys
import re
import yaml
from dateutil import parser
from dateutil.relativedelta import relativedelta
from datetime import datetime

now = datetime.now()
cur_month = now.month
interval_start = now.replace(day=27, hour=0, minute=0, second=0)
if interval_start < now:
    interval_end = interval_start
else:
    interval_end = interval_start - relativedelta(months=1)

interval_start = interval_end - relativedelta(months=1)

sys.stderr.write(f"Printing transactions from {interval_start} to {interval_end}\n")

class TxnPrinter:
    def __init__(self, date_idx, desc_idx, category_idx, debit_idx, negative_debit=False):
        self.date_idx = date_idx
        self.desc_idx = desc_idx
        self.category_idx = category_idx
        self.debit_idx = debit_idx
        self.matchers = []
        self.negative_debit = negative_debit

    def loadCategoryMap(self, path):
        with open(path, "r") as f:
            data = f.read()

        self.matchers = []
        for line in data.split("\n"):
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            field, category, regex_str = line.split(maxsplit=2)
            self.matchers.append((field, re.compile(regex_str), category))

    def printRow(self, row):
        date = parser.parse(row[self.date_idx])
        if (date > interval_end) or (date < interval_start):
            return False
        if row[self.debit_idx].strip() == "":
            return False
        debit = float(row[self.debit_idx])
        if self.negative_debit:
            debit = -debit
        if abs(debit) < 0.01:
            return False

        if self.category_idx:
            category = row[self.category_idx]
        else:
            category = ''
        for (field, regex, cat) in self.matchers:
            field = field.lower()
            if (field == "desc" and regex.match(row[self.desc_idx])):
                category = cat
                break
            if (field == "category" and self.category_idx and regex.match(row[self.category_idx])):
                category = cat
                break
        if category == "OMIT":
            sys.stderr.write(f"Omitting {row[self.desc_idx]} (${str(debit)})\n")
            return False

        desc = row[self.desc_idx].replace("\"", "")
        print(f"{date.strftime('%Y-%m-%d')}, \"{desc}\", {category}, {debit}")
        return True

filestats = {}
for path in sys.argv[1:]:
    filestats[path] = 0
    with open(path, encoding='latin1') as f:
        sys.stderr.write(f"Reading {path}\n")
        data = f.read().split('\n')
    
    if data[0].startswith("Note:"):
        header_idx = 2
    else:
        header_idx = 0

    with open(os.path.join(os.path.dirname(__file__), "./config/manifest.yaml")) as f:
      manifest = yaml.safe_load(f.read())

    hdr = dict([(v,i) for (i, v) in enumerate(data[header_idx].split(","))])
    printer = None
    for name, cfg in manifest.items():
      if cfg['match'] in hdr.keys():
          sys.stderr.write(f'Match on parser {name}\n')
          if cfg.get('pass', False):
            continue
          # 'Transaction Date', 'Posted Date', 'Card No.', 'Description', 'Category', 'Debit', 'Credit'
          printer = TxnPrinter(
                  date_idx = hdr[cfg['hdr']['date']],
                  desc_idx = hdr[cfg['hdr']['desc']],
                  category_idx = hdr.get(cfg['hdr']['category']),
                  debit_idx = hdr[cfg['hdr']['debit']],
                  negative_debit = cfg['negative_debit'],
                  )
          printer.loadCategoryMap(os.path.join(os.path.dirname(__file__), f"./config/{cfg['rules']}"))
          break

    if printer is None:
        sys.stderr.write(f"ERROR: origin of file {path} not resolved")
        sys.exit(1)

    for row in csv.reader(data[header_idx+1:]):
        if len(row) == 0:
            continue
        printed = printer.printRow(row)
        filestats[path] += 1 if printed else 0

sys.stderr.write(f"\n\n===================\nParsed {len(sys.argv[1:])} files:\n")
for k,v in filestats.items():
    sys.stderr.write(f"{k.ljust(40)}\t{v} items parsed\n")
