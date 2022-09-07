#!/usr/bin/python3
import re

def dict_incrase(dictc: dict,kay: str):
    try: dictc[kay]+=1
    except KeyError: dictc[kay]=1

def print_top(dict: dict, n: int):
    top=list(dict.items())
    top.sort(key=lambda x:-x[1])
    for i in range(n):
        print(f'{top[i][0]}\t{top[i][1]}')


f=open("access_log","r")

print()
ips=dict()
for i in f.readlines():
    for j in re.findall('(\d+\.\d+\.\d+\.\d+)', i):
        dict_incrase(ips,j)
print_top(ips,5)
f.seek(0)

print()
clients=dict()
for i in f.readlines():
    j = re.findall(r'\"[A-Za-z0-9,;\(\)_/ \\.:\?=&+%#\-]*\"', i)
    agent = j[-2].split()[0].replace('"',"")
    dict_incrase(clients,agent)

print_top(clients,5)
f.seek(0)


