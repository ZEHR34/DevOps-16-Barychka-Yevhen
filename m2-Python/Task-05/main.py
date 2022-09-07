#!/usr/bin/python3
import re

ips=dict()
f=open("access_log","r")
for i in f.readlines():
    for j in re.findall('(\d+\.\d+\.\d+\.\d+)', i):
        try: ips[j]+=1
        except KeyError:
            ips[j]=1
ipsansver=list(ips.items())
ipsansver.sort(key=lambda x:-x[1])
N=5
for i,j in ipsansver:
    print(f"{i}\t{j}")
    if N<=0:
        break
    N-=1


