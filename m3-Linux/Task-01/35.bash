#!/bin/bash

# 35
files=$(find img | grep .txt | awk -F/ '{print $(NF)}' | awk -F. '{print $1}')
images=$(find img | grep .jpg)

for i in $images;
do
  name=$(echo $i | awk -F/ '{print $(NF)}' | awk -F. '{print $1}')
  if [[ " ${files} " =~ " ${name} " ]]; then
    echo $i have .txt file
  else
    echo $i haven\'t .txt file
  fi
done

# 36
curl ifconfig.me
echo
hostname -I | awk '{print $1}'
