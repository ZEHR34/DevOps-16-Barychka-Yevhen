#!/usr/bin/python
import argparse
import string
from random import choice

parser = argparse.ArgumentParser()  # description='Process some integers.')
# parser.add_argument('integers', metavar='c', type=int, nargs='+',
#                     help='an integer for the accumulator')
parser.add_argument('-c', dest="count", default=1, type=int,
                    help='number of passwords')

parser.add_argument('-l', dest="length", type=int,
                    help='set length of password ')

parser.add_argument('-t', dest="template", type=str,
                    help='set template for generate passwords')

parser.add_argument('-f', dest="file", type=argparse.FileType('r'),
                    help='get list of patterns from file')


args = parser.parse_args()

if args.file:
    print(args.file.readlines())
    args.file.close()

#--------------------------
if args.length:
    for j in range(args.count):
        s = [choice(string.digits+string.ascii_lowercase+string.ascii_uppercase) for i in range(args.length)]
        print("".join(s))


def getRandomChar(template: str) -> str:
    k = 1
    if len(template) > 1:
        k = int(template[1:])
    elif len(template) < 1:
        return ""
    type = template[0]
    if type == "a":
        return "".join([choice(string.ascii_lowercase) for i in range(k)])
    elif type == "A":
        return "".join([choice(string.ascii_uppercase) for i in range(k)])
    elif type == "d":
        return "".join([choice(string.digits) for i in range(k)])
    elif type == "-":
        return "".join(["-" for i in range(k)])
    elif type == "@":
        return "".join(["@" for i in range(k)])
    else:
        raise Exception("uncorect template")


def genFromTemplate(template: str) -> str:
    template = unpackTemplate(template)
    a = template.split("%")
    try:
        a.remove("")
        a.remove("")
        a.remove("")
    except ValueError:
        pass
    password = [getRandomChar(i) for i in a]
    return "".join(password)


def unpackTemplate(template: str) -> str:
    try:
        begin = template.index("[")
        end = template.index("]")
    except ValueError:
        return template
    k = 1
    if template[end+1].isnumeric():
        k = int(template[end+1])
    types = template[begin+1:end].split("%")
    types.remove("")
    return template[:begin] + "%".join([choice(types) for _ in range(k)])+template[end+2:]



if args.template:
    print(genFromTemplate(args.template))

# print("digits: "+string.digits)
# print("punctuation: "+string.punctuation)
# print("ascii_lowercase: "+string.ascii_lowercase)
# print("ascii_uppercase: "+string.ascii_uppercase)
# print(string.digits+string.ascii_lowercase+string.ascii_uppercase)
