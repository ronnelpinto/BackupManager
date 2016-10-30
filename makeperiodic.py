import os
# run updatedb.py for every 10 secs to backup modified files
os.system('''
(
  while true
  do
    python3 updatedb.py
    sleep 10
  done
) &
disown''')
