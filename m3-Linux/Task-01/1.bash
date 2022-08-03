#!/usr/bin/bash

# 1
groups=`getent group | cut -d: -f3`
echo "" > groups.txt
for g in $groups
do
  echo $g >> groups.txt
done

# 2
fuser=entropia
fgroup=root
echo файли користувача $fuser і групи $fgroup
find  -group $fgroup -user $fuser

#3
echo
echo скрипти
find -iname "*.bash"

#4
echo
fuser=entropia
echo скрипти користувача $fuser
find -iname "*.bash" -user $fuser

