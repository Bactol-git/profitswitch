import os
import subprocess

os.system('systemctl --user stop profitswitch.service')
os.system('systemctl --user stop profitswitch_startup.service')

with open('PID_to_kill') as file:
    find_PID = file.readlines()

find_PID = find_PID[0]
find_PID = find_PID.replace('\n', '')

process = subprocess.run(find_PID, capture_output=True, text=True, shell=True)
process_to_kill = process.stdout

process_to_kill = process_to_kill.split('\n')
process_to_kill = list(filter(None, process_to_kill))

if len(process_to_kill) == 1:
    process_to_kill_run = str('sudo kill ') + process_to_kill[0]
if len(process_to_kill) == 2:
    process_to_kill_run = str('sudo kill ') + process_to_kill[0] + str(' ') + process_to_kill[1]

os.system(process_to_kill_run)

