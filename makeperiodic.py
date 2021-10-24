import os
os.system('''
(
  while true
  do
    python3 updatedb.py
    sleep 50
  done
) &
disown''')
# run updatedb.py for every 50 secs to backup modified files
# fix wait issue by increasing wait to 50 sec from 20 sec.
