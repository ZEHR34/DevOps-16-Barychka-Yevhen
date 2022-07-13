#!/usr/bin/python
import argparse
import string
from random import choice
from util import genFromTemplate

parser = argparse.ArgumentParser()

parser.add_argument('-c', dest="count", default=1, type=int,
                    help='number of passwords')

parser.add_argument('-l', dest="length", type=int,
                    help='set length of password ')

parser.add_argument('-t', dest="template", type=str,
                    help='set template for generate passwords')

parser.add_argument('-f', dest="file", type=argparse.FileType('r'),
                    help='get list of patterns from file')

args = parser.parse_args()

if args.length:
    for j in range(args.count):
        s = [choice(string.digits+string.ascii_lowercase+string.ascii_uppercase) for i in range(args.length)]
        print("".join(s))

if args.template:
    for i in range(args.count):
        print(genFromTemplate(args.template))

if args.file:
    for i in args.file.readlines():
        s = i.replace("\n", "")
        print(f"{s}: {genFromTemplate(s)}")
    args.file.close()
