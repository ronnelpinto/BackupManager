import os
os.system('''
(
  while true
  do
    python3 updatedb.py
    sleep 20
  done
) &
disown''')
# run updatedb.py for every 10 secs to backup modified files
# fix wait issue by increasing wait to 20 sec from 10 sec.
