import os
import subprocess
import json

with open('oc_config') as file:
    config= json.loads(file.read())

query = str('nvidia-smi --query-gpu=name --format=csv')

##number_of_gpus_temp = subprocess.run(query, capture_output=True, text=True, shell=True)
##number_of_gpus = number_of_gpus_temp.stdout
##
##number_of_gpus = number_of_gpus.split('\n')
##number_of_gpus = list(filter(None, number_of_gpus))
##number_of_gpus = len(number_of_gpus) -1

number_of_gpus = 2
print(number_of_gpus)


# make function that creates the OC file based on number of gpus

algo = 'rxd'

for element in config:
        if element['algo'] == algo:
                config = element

oc = str()


if len(config['power limit']) != number_of_gpus:
        print('Number of gpus in power limit config doesnt match number of gpus')

if len(config['lock core clock']) != number_of_gpus:
        print('Number of gpus in lock core clock config doesnt match number of gpus')

if len(config['core offset']) != number_of_gpus:
        print('Number of gpus in core offset config doesnt match number of gpus')

if len(config['memory offset']) != number_of_gpus:
        print('Number of gpus in memory offset config doesnt match number of gpus')

if len(config['lock memory']) != number_of_gpus:
        print('Number of gpus in lock memory config doesnt match number of gpus')


for x in range(number_of_gpus):
        if len(config['power limit']) > 1:
                pl = config['power limit'][x]
        else:
                pl = config['power limit'][0]
                
        if len(config['lock core clock']) > 1:
                lgc = config['lock core clock'][x]
        else:
                lgc = config['lock core clock'][0]
                
        if len(config['core offset']) > 1:
                coff = config['core offset'][x]
        else:
                coff = config['core offset'][0]
                
        if len(config['memory offset']) > 1:
                moff = config['memory offset'][x]
        else:
                moff = config['memory offset'][0]
                
        if len(config['lock memory']) > 1:
                memlock = config['lock memory'][x]
        else:
                memlock = config['lock memory'][0]
               
        if x == 0:
                oc = str('sudo nvidia-smi -pm ENABLED \nsudo nvidia-smi --rac\n')
        else:
                pass
        oc = oc + str('\nsudo nvidia-smi -i {x} --power-limit={pl} \nsudo nvidia-smi -i {x} --lock-gpu-clocks={lgc} \nsudo nvidia-settings -a [gpu:{x}]/GPUGraphicsClockOffset[4]={coff} \nsudo nvidia-settings -a [gpu:{x}]/GPUMemoryTransferRateOffset[4]={moff} \n').format(x=x,
                                                                                                                                                                                pl = pl,
                                                                                                                                                                                lgc = lgc,
                                                                                                                                                                                coff = coff,
                                                                                                                                                                                moff = moff)
        if memlock != 0:
                oc = oc + str('sudo nvidia-smi -i {x} --lmc {memlock}').format(x=x, memlock = memlock)
        

print(oc)

f = open('nvidia_OC', 'w')
f.write(oc)
f.close()
