#!/usr/bin/python
import argparse
import csv
from re import fullmatch


def in_range(diapason: [str], x: int) -> bool:
    """chek if x in range: ["1","3","5-6", ... ]"""
    if not diapason:
        return True
    range_select1 = [int(i) for i in diapason if i.isnumeric()]
    range_select2 = [list(range(int(i.split("-")[0]), int(i.split("-")[1]) + 1)) for i in diapason if
                     not i.isnumeric()]
    range_select2 = [int(j) for i in range_select2 for j in i]
    range_select = range_select1 + range_select2
    if x in range_select:
        return True
    else:
        return False


def in_filter(row: dict, regulars:[str]) -> bool:
    """is dict not conflict with list of regulars: ['key=regular','key2=regular2']"""
    if not regulars:
        return True
    for i in regulars:
        field, reg = i.split("=")
        if not fullmatch(reg, row[field]):
            return False
    return True


parser = argparse.ArgumentParser()

parser.add_argument('-s', dest="field", nargs='+',
                    help='set field to use')

parser.add_argument('-t', dest="reg", nargs='+',
                    help="set regulars to field -t user_name=User01 'IPv4=172.16.48.10\d'")

parser.add_argument('-r', dest="range", nargs='+',
                    help='set lines 1,2,3 and/or 1-3')

parser.add_argument('-f', dest="file", type=str, required=True,
                    help='csv file')

parser.add_argument('-e', dest="export_file", type=str,
                    help='csv file for export')

args = parser.parse_args()
file_name = args.file
keys = args.field
select_ranges = args.range
export_file = args.export_file
reg = args.reg

# filter data and extract to array
a = []
with open(file_name) as csvfile:
    reader = csv.DictReader(csvfile, quotechar="'")
    if not keys:
        keys = reader.fieldnames
    i = 0
    for row in reader:
        i += 1
        if in_range(select_ranges, i) and in_filter(row, reg):
            a.append([row[j] for j in keys])

# export data to file or print
if export_file:
    data = [dict(zip(keys, i)) for i in a]
    with open(export_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=keys, quotechar="'")
        writer.writeheader()
        writer.writerows(data)
else:
    print(keys)
    for i in a:
        print(i)

# ./csvParser.py -s hostname IPv4 user_name -r 1-3 -f file.csv -t 'user_name=User0\d' 'IPv4=172.16.48.10[12]' -e test.csv
