import os
import subprocess

os.system('systemctl --user stop profitswitch.service')

with open('PID_to_kill') as file:
    find_PID = file.readlines()

find_PID = find_PID[0]
find_PID = find_PID.replace('\n', '')

process = subprocess.run(find_PID, capture_output=True, text=True, shell=True)
process_to_kill = process.stdout

process_to_kill = process_to_kill.split('\n')
process_to_kill = list(filter(None, process_to_kill))

base = str('sudo kill')

for x in process_to_kill:
    if x == process_to_kill[0]:
        process_to_kill_run = base + str (' ') + str(x)
    else:
        process_to_kill_run = process_to_kill_run + str(' ') + str(x)  

os.system(process_to_kill_run)

