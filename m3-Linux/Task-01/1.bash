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


# 7-8
ffile='test/f1'
echo
echo посилання на $ffile
ls $ffile
find -L  -samefile $ffile 2>/dev/null

# 9-10
finode=1055356
echo
echo розташування файлу з inode $finode
find -inum $finode 2> /dev/null

# 11
echo
fdir='test'
cd $fdir
touch "t1"
ln -s t1 t2
ln t1 t3
cd '../'
echo створено t1 t2 t3
ls $fdir -i
ffile='test/f1'
fdell=`find -L  -samefile "$fdir/t1" 2>/dev/null`
for i in $fdell
do
  rm $i
done
echo видалено t1 t2 t3
ls $fdir -i

# 12
fdir="test"
fmod=333
echo
files=`ls $fdir -p | grep -v /`
for i in $files
do
  chmod $fmod "$fdir/$i"
done
echo змінено прова на $fmod у дерикторії $fdir
