import requests
import json
import os
import subprocess
import time

with open('config') as file:
    conf= file.read()
    
config=json.loads(conf)

terrahash = 1000000000000
megahash = 1000000
seconds_a_day = 60*60*24

power_rate = config['power_rate']

def api_fetch(url_link):
    for x in (range(3)):
        try:
            temp = json.loads(requests.get(url_link, timeout=2).text)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
        try:
            e
        except NameError:
            break
    return temp


stats = [{'algo': 'eth', 'price': float(api_fetch('https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=ETHUSDT')['data']['c']),
                  'diff': int(api_fetch('https://api.minerstat.com/v2/coins?list=ETH')[0]['difficulty']),
                  'block_time': float(api_fetch('https://whattomine.com/coins/151.json?hr=244.0&p=1040.0&fee=0.0&cost=0.1&cost_currency=USD&hcost=0.0&span_br=1h&span_d=24')['block_time']),
                  'block_reward': 2},
                 {'algo': 'flux', 'price': float(api_fetch('https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=FLUXUSDT')['data']['c']),
                  'diff': int(api_fetch('https://api.runonflux.io/daemon/getmininginfo')['data']['difficulty']),
                  'block_time': 120,
                  'block_reward': 37.5},
                  {'algo': 'erg', 'price': float(api_fetch('https://www.coingecko.com/price_charts/2484/usd/24_hours.json')['stats'][-1][1]),
                  'diff': int(api_fetch('https://api.ergoplatform.com/blocks?limit=1&offset=0&sortBy=height&sortDirection=desc')['items'][0]['difficulty']),
                  'block_time': 120,
                  'block_reward': 48},
                 {'algo': 'etc', 'price': float(api_fetch('https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=ETCUSDT')['data']['c']),
                  'diff': int(api_fetch('https://api.minerstat.com/v2/coins?list=ETC')[0]['difficulty']),
                  'block_time': 120,
                  'block_reward': 2.48},
                 {'algo': 'rvn', 'price': float(api_fetch('https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=RVNUSDT')['data']['c']),
                  'diff': int(api_fetch('https://explorer.mangofarmassets.com/api/status?q=getInfo')['info']['difficulty']),
                  'block_time': 60,
                  'block_reward': 2500},
                 {'algo': 'firo', 'price': float(api_fetch('https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=FIROUSDT')['data']['c']),
                  'diff': int(api_fetch('https://api.minerstat.com/v2/coins?list=FIRO')[0]['difficulty']),
                  'block_time': 150,
                  'block_reward': 1.5625}
                 ]

# Reward calculations

HR_req_eth = stats[0]['diff']/stats[0]['block_time']
eth_est_revenue_th = (stats[0]['block_reward']*(seconds_a_day/stats[0]['block_time']))/HR_req_eth
eth_est_revenue = ((config['eth']['hash']*megahash))*eth_est_revenue_th
eth_est_revenue_usd = eth_est_revenue * stats[0]['price']
eth_cost = (config['eth']['power']/1000)*24*(power_rate)
eth_est_reward = eth_est_revenue_usd - eth_cost

HR_req_flux = stats[1]['diff']*10000/stats[1]['block_time']
flux_est_revenue_th = (stats[1]['block_reward']*config['flux_PA_multiplier']*(seconds_a_day/stats[1]['block_time']))/HR_req_flux
flux_est_revenue = ((config['flux']['hash']))*flux_est_revenue_th
flux_est_revenue_usd = flux_est_revenue * stats[1]['price']
flux_cost = (config['flux']['power']/1000)*24*(power_rate)
flux_est_reward = flux_est_revenue_usd - flux_cost

HR_req_erg = stats[2]['diff']/stats[2]['block_time']
erg_est_revenue_th = (stats[2]['block_reward']*(seconds_a_day/stats[2]['block_time']))/HR_req_erg
erg_est_revenue = ((config['erg']['hash']*megahash))*erg_est_revenue_th
erg_est_revenue_usd = erg_est_revenue * stats[2]['price']
erg_cost = (config['erg']['power']/1000)*24*(power_rate)
erg_est_reward = erg_est_revenue_usd - erg_cost

HR_req_etc = stats[3]['diff']/stats[3]['block_time']
etc_est_revenue_th = (stats[3]['block_reward']*(seconds_a_day/stats[3]['block_time']))/HR_req_etc
etc_est_revenue = ((config['eth']['hash']*megahash))*etc_est_revenue_th
etc_est_revenue_usd = etc_est_revenue * stats[3]['price']
etc_est_reward = etc_est_revenue_usd - eth_cost

HR_req_rvn = (stats[4]['diff']*2**32)/stats[4]['block_time']
rvn_est_revenue_th = (stats[4]['block_reward']*(seconds_a_day/stats[4]['block_time']))/HR_req_rvn
rvn_est_revenue = ((config['rvn']['hash']*megahash))*rvn_est_revenue_th
rvn_est_revenue_usd = rvn_est_revenue * stats[4]['price']
rvn_cost = (config['rvn']['power']/1000)*24*(power_rate)
rvn_est_reward = rvn_est_revenue_usd - rvn_cost

HR_req_firo = (stats[5]['diff']*2**32)/stats[5]['block_time']
firo_est_revenue_th = (stats[5]['block_reward']*(seconds_a_day/stats[5]['block_time']))/HR_req_firo
firo_est_revenue = ((config['rvn']['hash']*megahash))*firo_est_revenue_th
firo_est_revenue_usd = firo_est_revenue * stats[5]['price']
firo_cost = (config['rvn']['power']/1000)*24*(power_rate)
firo_est_reward = firo_est_revenue_usd - firo_cost

# Choose what algo to mine
highest_profit = max((eth_est_reward, flux_est_reward, erg_est_reward, etc_est_reward, rvn_est_reward, firo_est_reward))

if highest_profit >= 0.01:
    new_algo = ()
    if eth_est_reward == highest_profit:
        new_algo = 'eth'
    if flux_est_reward == highest_profit:
        new_algo = 'flux'
    if erg_est_reward == highest_profit:
        new_algo = 'erg'
    if etc_est_reward == highest_profit:
        new_algo = 'etc'
    if rvn_est_reward == highest_profit:
        new_algo = 'rvn'
    if firo_est_reward == highest_profit:
        new_algo = 'firo'
    else:
        pass

        

    # Select start script
    start_miner = str('./profitswitch_') + new_algo

    if config['cards'] == 'amd':
        start_OC = str('sudo ./overclocks/amd_OC_') + new_algo
    if config['cards'] == 'nvidia':
        start_OC = str('sudo ./overclocks/nvidia_OC_') + new_algo
    if config['cards'] == 'mixed':
        start_OC = str('sudo ./overclocks/amd_OC_') + new_algo + str(' && sudo .&(pwd)/overclocks/nvidia_OC_') + new_algo

    print(start_miner)


    # kill earlier miner if new algo != current algo
    try:
        with open('current_algo') as f:
            current_algo = f.readlines()
    except Exception:
        current_algo = ['']


    if current_algo[0] != new_algo:
        #kill current miner
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
        if len(process_to_kill) >= 1:        
            try:
                os.system(process_to_kill_run)
            except Exception as e:
                print(e)

        # start new miner
        time.sleep(5)
        wd = subprocess.run('pwd', capture_output=True, text=True)
        wd = wd.stdout
        wd = wd.strip()
        try:
            os.system(start_OC)
            subprocess.Popen(['sudo',start_miner], shell=False, cwd=wd)
            with open('current_algo', 'w') as f:
                f.write(new_algo)
        except Exception as e:
            print(e)      
    
    else:
        with open('PID_to_kill') as file:
            find_PID = file.readlines() 

        find_PID = find_PID[0]
        find_PID = find_PID.replace('\n', '')

        process = subprocess.run(find_PID, capture_output=True, text=True, shell=True)
        process_to_kill = process.stdout

        if process_to_kill == '':
            subprocess.Popen(['sudo',start_miner], shell=False, cwd=wd)
else:
    new_algo = 'Better off not mining'
