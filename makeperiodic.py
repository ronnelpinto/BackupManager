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
# fixing wait issue by adding 20 sec wait instead of 10 sec.
