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

# 6
function myfunc {
  size1=`ls -l $1 | awk '{print $5}'`
  size2=`ls -l $2 | awk '{print $5}'`
  if (( $size1==$size2 )) && [[ "$1" != "$2" ]]; then
    if [[ `md5sum $1 | awk '{print $1}'` = `md5sum $2 | awk '{print $1}'` ]]; then
      echo same file $1 and $2
    fi
  fi
}
echo
fdir=`ls -p | grep -v /`
for i in $fdir
do
  for j in $fdir
  do
    myfunc $i $j
  done
done


# 7
ffile='test/f1'
ls $ffile
find -L  -samefile $ffile 2>/dev/null
#find -L / -samefile test/f1 2>/dev/null
