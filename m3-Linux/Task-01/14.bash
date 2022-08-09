#!/bin/bash

# 14
cat /sys/class/net/*/address

# 15
users

# 16
netstat -t

#17
echo 123 > test.txt
echo qwerty > test2.txt
ln -s test.txt testlink.txt
ln -sfn test2.txt testlink.txt
rm test.txt test2.txt testlink.txt