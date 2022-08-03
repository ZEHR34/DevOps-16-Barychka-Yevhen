#/usr/bin/bash

OLD='pam_unix.so obscure use_authtok try_first_pass yescrypt'
NEW="$OLD minlen=8 dcredit=-1 ocredit=-1 minclass=2"
FILE='/etc/pam.d/common-password'

echo $NEW

if [ "$1" == "b"  ] || [ $# -gt 1  ]; then
          echo "Parameter 1 is empty"
          sed -i -e "s/$NEW/$OLD/g" "$FILE"
else
          sed -i -e "s/$OLD\$/$NEW/g" "$FILE"
fi
