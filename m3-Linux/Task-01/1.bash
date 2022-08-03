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

# 3
echo
echo скрипти
find -iname "*.bash"

# 4
fuser=entropia
echo
echo скрипти користувача $fuser
find -iname "*.bash" -user $fuser

# 5
ftype="txt"
ftext="text"
echo
echo файли $ftype які місять  $ftext
ftype='*.'$ftype
find . -name "$ftype" -exec grep -i "$ftext" {} \; -print


