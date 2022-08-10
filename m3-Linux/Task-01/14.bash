#!/bin/bash

# 14
cat /sys/class/net/*/address

# 15
users

# 16
netstat -t

# 17
echo 123 > test.txt
echo qwerty > test2.txt
ln -s test.txt testlink.txt
ln -sfn test2.txt testlink.txt
rm test.txt test2.txt testlink.txt

# 18
mkdir "testf"
pathf="./testf"
echo 1234 > testf/1.txt
echo qwer > testf/2.txt
mkdir "testlfInks"
for i in `ls $pathf`
do
  ln -s ../$pathf/$i testlfInks/$i
done
rm -r testlfInks testf -r

# 19-20-21
mkdir test
echo 123 > test/1
ln -s ../test/1 test/2
ln test/1 test/3
cp -rLp test testL
rm -r test testL

# 22
for i in `find ! -name . -prune -type l`; do
  ln -sf "$(readlink -f "$i")" "$i"
done

#23
find . -type l | while read l; do
    target="$(realpath "$l")"
    ln -fs "$(realpath --relative-to="$(dirname "$(realpath -s "$l")")" "$target")" "$l"
done

# 24
for i in `find ! -name . -prune -type l`; do
  rm "$i"
done

# 25
touch 1
touch 2
tar -cf 1.tar 1 2
rm 1 2
tar -xf 1.tar 1
rm 1.tar 1

# 26
tar -cvpf 1.tar 1 2> /dev/null
rm 1.tar
# 27
find ./1 -type d -links 2 -exec mkdir -p "backup/{}" \;

# 28
awk -F: '{ print $1}' /etc/passwd | sort

# 29
awk -F: '{ print $3 "  " $1}' /etc/passwd | sort -n

# 30
awk -F: '{ print $3 "  " $1}' /etc/passwd | sort -nr

# 31
grep nologin /etc/passwd | awk -F: '{ print $3 "  " $1}' | sort -n
grep -v nologin /etc/passwd | awk -F: '{ print $3 "  " $1}' | sort -n

# 32
grep '/bash\|/sh\|/zsh' /etc/passwd
grep -v '/bash\|/sh\|/zsh' /etc/passwd
