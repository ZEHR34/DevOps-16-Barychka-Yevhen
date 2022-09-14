#!/usr/bin/python3
import re

def dict_incrase(dictc: dict,kay: str):
    try: dictc[kay]+=1
    except KeyError: dictc[kay]=1

def print_top(dict: dict, n: int):
    top=list(dict.items())
    top.sort(key=lambda x:-x[1])
    for i in range(min(n,len(top))):
        print(f'{top[i][0]}\t{top[i][1]}')


f = open("access_log", "r")

print()
print("5 найчастіших ip")
ips=dict()
for i in f.readlines():
    for j in re.findall('(\d+\.\d+\.\d+\.\d+)', i):
        dict_incrase(ips,j)
print_top(ips,5)
f.seek(0)

print()
print("5 найчастіших User-Agent")
clients=dict()
for i in f.readlines():
    j = re.findall(r'\"[A-Za-z0-9,;\(\)_/ \\.:\?=&+%#\-]*\"', i)
    agent = j[-2].split()[0].replace('"', "")
    dict_incrase(clients, agent)

print_top(clients,5)
f.seek(0)

print()
print("5 найзавантажиніших хвилин")
time=dict()
for i in f.readlines():
    j = re.findall(r'08/Oct/2015:09:\d{2}:\d{2}', i)[0]
    dict_incrase(time, j)

print_top(time,5)
f.seek(0)

print()
print("годтини з найчастішими 500 СК")
errors = dict()
for i in f.readlines():
    j = re.findall(r'\[08/Oct/2015:\d\d:\d\d:\d\d [+-]00\d\d\] \"[A-Za-z0-9,;\(\)_/ \\.:\?=&+%#\-]*\" 5\d\d', i)
    if j:
        # print(j[0].split()[0][1:])
        dict_incrase(errors, j[0].split()[0][1:-3])

print_top(errors, 5)
f.seek(0)



print()
print("5 накорочих запитів")
queset=[]
for i in f.readlines():
    j = re.findall(r'\"[A-Za-z0-9,;\(\)_/ \\.:\?=&+%#!\-]*\"', i)[0]
    if not (j in queset):
        queset.append(j)
        queset.sort(key=lambda x:len(x))
        queset=queset[:5]
print("\n".join(queset))
f.seek(0)


print()
print("5 найчастіших запитів з точністю до 2-ого /")
quests_url=dict()
for i in f.readlines():
    j = re.findall(r'\"[A-Za-z0-9,;\(\)_/ \\.:\?=&+%#\-]*\"', i)[0]
    j = j.split("/")[1:3]
    j = "/".join(j)
    dict_incrase(quests_url, j)
print_top(quests_url, 5)
f.seek(0)


print()
print("5 найактивніших воркерів")
workers=dict()
for i in f.readlines():
    j = re.findall(r'\"[A-Za-z0-9,;\(\)_/ \\.:\?=&+%#\-]*\"', i)[-1]
    dict_incrase(workers, j)
print_top(workers, 5)
f.seek(0)

print()
print("5 найчастіших переходів")
redirects = dict()
for i in f.readlines():
    j = re.findall(r'\"[A-Za-z0-9,;\(\)_/ \\.:\?=&+%#!\-]*\"', i)[1]
    dict_incrase(redirects,j)
print_top(redirects,5)
f.seek(0)


def time_round(time: str, quant:int) -> str:
    minutest = time.split(":")[-2:]
    sec = int(minutest[1])+60*int(minutest[0])
    time_step=[0, 0]
    min=sec//quant*quant
    time_step[0] = str(min // 60)
    if len(time_step[0])==1:
        time_step[0]="0"+time_step[0]
    time_step[1] = str(min % 60)
    if len(time_step[1])==1:
        time_step[1]="0"+time_step[1]
    unsver = ":".join( time.split(":")[:-2]+time_step )
    return unsver


print()
print("5 найчастіших воркерів в період 5хв")
timeWorker = dict()
for i in f.readlines():
    j = re.findall(r'\"[A-Za-z0-9,;\(\)_/ \\.:\?=&+%#!\-]*\"', i)[-1]
    t = re.findall(r'08/Oct/2015:\d\d:\d\d:\d\d',i)[0]
    t = time_round(t, 60*5)
    dict_incrase(timeWorker, t+" "+j)
print_top(timeWorker, 5)
f.seek(0)


print()
print("5 найчастіших воркерів в період 1хв")
timeWorker = dict()
for i in f.readlines():
    j = re.findall(r'\"[A-Za-z0-9,;\(\)_/ \\.:\?=&+%#!\-]*\"', i)[-1]
    t = re.findall(r'08/Oct/2015:\d\d:\d\d:\d\d',i)[0]
    t = time_round(t, 60)
    dict_incrase(timeWorker, t+" "+j)
print_top(timeWorker, 5)
f.seek(0)


print()
print("5 найчастіших воркерів в період 30c")
timeWorker = dict()
for i in f.readlines():
    j = re.findall(r'\"[A-Za-z0-9,;\(\)_/ \\.:\?=&+%#!\-]*\"', i)[-1]
    t = re.findall(r'08/Oct/2015:\d\d:\d\d:\d\d',i)[0]
    t = time_round(t, 30)
    dict_incrase(timeWorker, t+" "+j)
print_top(timeWorker, 5)
f.seek(0)


print()
print("найбільше запитів за 1хв")
timeQuests = dict()
for i in f.readlines():
    t = re.findall(r'08/Oct/2015:\d\d:\d\d:\d\d',i)[0]
    t = time_round(t, 60)
    dict_incrase(timeQuests, t)
print_top(timeQuests, 5)
f.seek(0)

print()
print("найбільше запитів за 2хв")
timeQuests = dict()
for i in f.readlines():
    t = re.findall(r'08/Oct/2015:\d\d:\d\d:\d\d',i)[0]
    t = time_round(t, 60*2)
    dict_incrase(timeQuests, t)
print_top(timeQuests, 5)
f.seek(0)

print()
print("найбільше запитів за 3хв")
timeQuests = dict()
for i in f.readlines():
    t = re.findall(r'08/Oct/2015:\d\d:\d\d:\d\d',i)[0]
    t = time_round(t, 60*3)
    dict_incrase(timeQuests, t)
print_top(timeQuests, 5)
f.seek(0)
