#!/bin/bash

function containsElement () {
  echo $1 $2
  local e match="$1"
  shift
  for e; do [[ "$e" == "$match" ]] && return 0; done
  return 1
}

mkdir "test1" 2> /dev/null
mkdir "test1/test1d" 2> /dev/null
mkdir "test1/test1m" 2> /dev/null


mkdir "test2" 2> /dev/null
mkdir "test2/test1d" 2> /dev/null


echo 1234 > test1/test.txt
echo 1234 > test2/test.txt

echo 1234 > test1/dif.txt
echo 12345 > test2/dif.txt


function traverse() {
for file in `ls $1`
do
    if [ ! -d "$1/$file" ] ; then
        if diferent=$(diff $1/$file $2/$file 2> /dev/null); then
            echo $1/$file is singl
        fi
        if [[ $diferent != "" ]];then
            echo $1/$file and $2/$file is diferent
            diff $1/$file $2/$file
        fi
    else
        if (ls $1/$file $2/$file &> /dev/null); then
            traverse $1/$file $2/$file
        else
          echo dir $1/$file is singl
        fi
    fi
done
}


traverse "test1" "test2"
