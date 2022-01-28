# Expense Tools

This is a collection of simple scripts and utilities to collect, annotate, and export expenses from individual sources.

## Expense Parser

Parse CSV dumps of expenses from Splitwise, credit card companies etc.

Configs are located in `expense_parser/config`:

* `manifest.yaml` selects a specific rule CSV file based on a matching header column. It also contains parsing config and mapping of header names to useful columns.
* `*.csv` files are a list of manual rules that normalize the categories provided by each input CSV.
  * The first column is what to match on (e.g. category vs description), the second is the category to write, and the third is a regular expression for matching the particular category or description text.
  * Rules are evaluated in descending order, so earlier rules match first.

Installation: `cd expense_parser && pip3 install -r requirements.txt`

To use the parser, run `python3 parse_expenses.py input1.csv input2.csv...`.

If you wish to write the output for later upload (e.g. to a Google Sheet), append ` > out.csv` to the command above. Log messages are written to stderr, so only output rows are writen to the file (via stdout).

## Price Fetcher

Fetch prices of specific goods to help with computing a personal [Consumer Price Index](https://en.wikipedia.org/wiki/Consumer_price_index). 

Items and queries are currently quite hardcoded. 
