#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser()  # description='Process some integers.')
# parser.add_argument('integers', metavar='c', type=int, nargs='+',
#                     help='an integer for the accumulator')
parser.add_argument('-c', dest="count", default=1, type=int,
                    help='number of passwords')

parser.add_argument('-l', dest="len", type=int,
                    help='set length of password ')

parser.add_argument('-t', dest="template", type=str,
                    help='set template for generate passwords')

parser.add_argument('-f', dest="file", type=argparse.FileType('r'),
                    help='get list of patterns from file')


args = parser.parse_args()

if args.file:
    print(args.file.readlines())
    args.file.close()

