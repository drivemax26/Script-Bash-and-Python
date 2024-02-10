#!/bin/bash

current_date=$(date +%s)

users=$(awk -F ':' '$3 > 1000 {print $1}' /etc/passwd)

for user in $users; do

  last_login_date=$(lastlog -u "$user" | awk 'NR==2 {print $5, $6, $7, $8, $9}')

  days_since_last_login=$(( ($current_date - $(date -d "$last_login_date" +%s)) / 86400 ))

  if [ $days_since_last_login -gt 30 ]; then
    userdel -r "$user"
  fi
done