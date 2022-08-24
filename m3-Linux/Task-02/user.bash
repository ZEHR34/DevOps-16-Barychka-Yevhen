#/usr/bin/bash


UNAME=iptableuser
useradd -m $UNAME
echo "alias iptables='sudo /sbin/iptables'" | sudo -u ${UNAME} -H tee /home/${UNAME}/.bash_aliases
usermod -aG sudo $UNAME
usermod -aG root $UNAME




