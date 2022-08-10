#!/bin/bash

# 33
curl -s localhost:8000 | sed -n 's/.*href="\([^"]*\).*/\1/p'
wget -q -O - localhost:8000 | sed -n 's/.*href="\([^"]*\).*/\1/p'

# 34
ps -eo pid,user,cmd,time --sort=-time | head
