import delivery
import gianteagle
import hatchbox
import metals
import redstart
import traderjoes
import winespirits
import walmart
import riogrande
import sys

if __name__ == "__main__":
    results = []
    for i in [delivery, gianteagle, hatchbox, metals, redstart, traderjoes, winespirits, walmart, riogrande]:
        sys.stderr.write("Querying %s\n" % i.__name__)
        results += i.all_queries()
    
    results.sort(key=lambda i: i[0])
    for r in results:
        print(r[0].replace(",",""),",",r[1])
