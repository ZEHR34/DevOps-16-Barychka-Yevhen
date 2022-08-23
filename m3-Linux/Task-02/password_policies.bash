#/usr/bin/bash

OLD='pam_unix.so obscure use_authtok try_first_pass yescrypt'
NEW="$OLD minlen=8 dcredit=-1 ocredit=-1 minclass=2 remember=3"
FILE='/etc/pam.d/common-password'


sed -i -e "s/$OLD\$/$NEW/g" "$FILE"


FILE2='/etc/login.defs'

sed -i -e "s/PASS_MAX_DAYS\t99999/PASS_MAX_DAYS\t90/g" "$FILE2"
sed -i -e "s/PASS_WARN_AGE\t7/PASS_WARN_AGE\t0/g" "$FILE2"
