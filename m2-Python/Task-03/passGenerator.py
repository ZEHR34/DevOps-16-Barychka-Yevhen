#!/usr/bin/python
import argparse
import string
from random import choice
from util import genFromTemplate
import logging

parser = argparse.ArgumentParser()

parser.add_argument('-c', dest="count", default=1, type=int,
                    help='number of passwords')

parser.add_argument('-l', dest="length", type=int,
                    help='set length of password ')

parser.add_argument('-t', dest="template", type=str,
                    help='set template for generate passwords')

parser.add_argument('-f', dest="file", type=argparse.FileType('r'),
                    help='get list of patterns from file')

parser.add_argument('-v', dest="verbose", action='count', default=0)

args = parser.parse_args()

args.verbose = 70 - (10*(args.verbose+3)) if args.verbose > 0 else 70
logging.basicConfig(level=args.verbose, format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


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
