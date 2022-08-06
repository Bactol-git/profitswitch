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



for x in range(3):
    try:
        stats = [{'algo': 'eth', 'price': float(json.loads(requests.get('https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=ETHUSDT', timeout=2).text)['data']['c']),
                  'diff': int(json.loads(requests.get('https://api.minerstat.com/v2/coins?list=ETH').text)[0]['difficulty']),
                  'block_time': float(json.loads(requests.get('https://whattomine.com/coins/151.json?hr=244.0&p=1040.0&fee=0.0&cost=0.1&cost_currency=USD&hcost=0.0&span_br=1h&span_d=24', timeout=2).text)['block_time']),
                  'block_reward': 2},
                 {'algo': 'flux', 'price': float(json.loads(requests.get('https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=FLUXUSDT', timeout=2).text)['data']['c']),
                  'diff': int(json.loads(requests.get('https://api.runonflux.io/daemon/getmininginfo', timeout=2).text)['data']['difficulty']),
                  'block_time': 120,
                  'block_reward': 37.5},
                 {'algo': 'erg', 'price': float(json.loads(requests.get('https://www.coingecko.com/price_charts/2484/usd/24_hours.json', timeout=2).text)['stats'][-1][1]),
                  'diff': int(json.loads(requests.get('https://api.ergoplatform.com/blocks?limit=1&offset=0&sortBy=height&sortDirection=desc', timeout=2).text)['items'][0]['difficulty']),
                  'block_time': 120,
                  'block_reward': 48},
                 {'algo': 'etc', 'price': float(json.loads(requests.get('https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=ETCUSDT', timeout=2).text)['data']['c']),
                  'diff': int(json.loads(requests.get('https://api.minerstat.com/v2/coins?list=ETC', timeout=2).text)[0]['difficulty']),
                  'block_time': 120,
                  'block_reward': 2.48},
                 {'algo': 'rvn', 'price': float(json.loads(requests.get('https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=RVNUSDT', timeout=2).text)['data']['c']),
                  'diff': int(json.loads(requests.get('https://explorer.mangofarmassets.com/api/status?q=getInfo', timeout=2).text)['info']['difficulty']),
                  'block_time': 60,
                  'block_reward': 2500},
                 {'algo': 'firo', 'price': float(json.loads(requests.get('https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=FIROUSDT', timeout=2).text)['data']['c']),
                  'diff': int(json.loads(requests.get('https://api.minerstat.com/v2/coins?list=FIRO', timeout=2).text)[0]['difficulty']),
                  'block_time': 150,
                  'block_reward': 1.5625}
                ]
                 
    except Exception as e:
        print(e)
        continue
    try:
        e
    except NameError:
        break
    else:
        time.sleep(5)

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

    
print('ETH:  ', round(eth_est_reward,2))
print('FLUX: ',round(flux_est_reward,2))
print('ERG:  ', round(erg_est_reward,2))
print('ETC:  ', round(etc_est_reward,2))
print('RVN:  ', round(rvn_est_reward,2))
print('FIRO:  ', round(firo_est_reward,2))
