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
    for i in regulars:
        fild, reg = i.split("=")
        if not fullmatch(reg, row[fild]):
            # print(fild,reg,"**********************")
            return False
        # print(fild, reg)
    return True


parser = argparse.ArgumentParser()

# parser.add_argument('-c', dest="count", default=1, type=int,
#                     help='number of passwords')
#
# parser.add_argument('-l', dest="length", type=int,
#                     help='set length of password ')

parser.add_argument('-s', dest="field", nargs='+',
                    help='set field to use')

parser.add_argument('-t', dest="reg", nargs='+',
                    help='set regulars to field')

parser.add_argument('-r', dest="range", nargs='+',
                    help='set lines 1,2,3 and/or 1-3')

parser.add_argument('-f', dest="file", type=str,
                    help='csv file')

# parser.add_argument('-v', dest="verbose", action='count', default=0)

args = parser.parse_args()

# parser.add_argument('--head', dest="heading", default=1, type=bool,
#                     help='head in csv file of passwords')



# ./csvParser.py -s hostname IPv4 user_name -r 1-3 -f file.csv -t user_name=User01 'IPv4=172.16.48.10\d'
# print(args.file)
file_name = args.file
keys = args.field
print(keys)


# print(args.reg)


with open(file_name) as csvfile:
    reader = csv.DictReader(csvfile, quotechar="'")
    b = reader.fieldnames
    a = []
    i = 0
    for row in reader:
        i += 1
        # print(row["user_name"] + str(in_filter(row, args.reg)))
        if in_range(args.range, i) and in_filter(row, args.reg):
            a.append([row[i] for i in keys])

for i in a: print(i)