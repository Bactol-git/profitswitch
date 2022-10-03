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
            temp = json.loads(requests.get(url_link, timeout=3).text)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
        try:
            e
        except NameError:
            return temp
            break

    
urls = [{'algo': 'cfx', 'price': 'https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=CFXUSDT',
                  'diff': 'https://confluxscan.net/v1/block?limit=10&skip=0'},
                 {'algo': 'flux', 'price':'https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=FLUXUSDT',
                  'diff': 'https://api.runonflux.io/daemon/getmininginfo'},
                  {'algo': 'erg', 'price': 'https://www.coingecko.com/price_charts/2484/usd/24_hours.json',
                  'diff': 'https://api.ergoplatform.com/blocks?limit=1&offset=0&sortBy=height&sortDirection=desc'},
                 {'algo': 'etc', 'price': 'https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=ETCUSDT',
                  'diff': 'https://api.minerstat.com/v2/coins?list=ETC'},
                 {'algo': 'rvn', 'price': 'https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=RVNUSDT',
                  'diff': 'https://explorer.mangofarmassets.com/api/status?q=getInfo'},
                 {'algo': 'firo', 'price': 'https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=FIROUSDT',
                  'diff': 'https://api.minerstat.com/v2/coins?list=FIRO'},
                 {'algo': 'ethw', 'price': 'https://ftx.com/api/markets/ETHW/USD',
                  'diff': 'https://iceberg.ethwmine.com/api/stats'}
                 ]



cfx_price_temp = api_fetch(urls[0]['price'])
cfx_diff_temp = api_fetch(urls[0]['diff'])
flux_price_temp = api_fetch(urls[1]['price'])
flux_diff_temp = api_fetch(urls[1]['diff'])
erg_price_temp = api_fetch(urls[2]['price'])
erg_diff_temp = api_fetch(urls[2]['diff'])
etc_price_temp = api_fetch(urls[3]['price'])
etc_diff_temp = api_fetch(urls[3]['diff'])
rvn_price_temp = api_fetch(urls[4]['price'])
rvn_diff_temp = api_fetch(urls[4]['diff'])
firo_price_temp = api_fetch(urls[5]['price'])
firo_diff_temp = api_fetch(urls[5]['diff'])
ethw_price_temp = api_fetch(urls[6]['price'])
ethw_diff_temp = api_fetch(urls[6]['diff'])


try:
    cfx_price = float(cfx_price_temp['data']['c'])
except Exception as e:
    print(e)
    cfx_price = 0
try:
    cfx_diff = int(cfx_diff_temp['data']['list'][0]['difficulty'])
except Exception:
    cfx_diff = 0

cfx_block_time = 0.5
cfx_block_reward = 2

try:
    flux_price = float(flux_price_temp['data']['c'])
except Exception:
    flux_price = 0
try:
    flux_diff = int(flux_diff_temp['data']['difficulty'])
except Exception:
    flux_diff = 0
flux_block_time = 120
flux_block_reward = 37.5

try:
    erg_price = float(erg_price_temp['stats'][-1][1])
except Exception:
    erg_price = 0
try:
    erg_diff = int(erg_diff_temp['items'][0]['difficulty'])
except Exception:
    erg_diff = 0
erg_block_time = 120
try:
    erg_block_reward = float(erg_diff_temp['items'][0]['minerReward'])/1000000000
except Exception:
    erg_block_reward = 0.00000001
    
try:
    etc_price = float(etc_price_temp['data']['c'])
except Exception:
    etc_price = 0
try:
    etc_diff = int(etc_diff_temp[0]['difficulty'])
except Exception:
    etc_diff = 0
etc_block_time = 13
try:
    etc_block_reward = float(etc_diff_temp[0]['reward_block'])
except Exception:
    etc_block_reward = 0.00000001
    
try:
    rvn_price = float(rvn_price_temp['data']['c'])
except Exception:
    rvn_price = 0
try:
    rvn_diff = int(rvn_diff_temp['info']['difficulty'])
except Exception:
    rvn_diff = 0
rvn_block_time = 60
try:
    rvn_block_reward = float(rvn_diff_temp['info']['reward'])/100000000
except Exception:
    rvn_block_reward = 0.00000001

try:
    firo_price = float(firo_price_temp['data']['c'])
except Exception:
    firo_price = 0
try:
    firo_diff = int(firo_diff_temp[0]['difficulty'])
except Exception:
    firo_diff = 0
firo_block_time = 150
try:
    firo_block_reward = float(firo_diff_temp[0]['reward_block'])
except Exception:
    firo_block_reward = 0.00000001

try:
    ethw_price = float(ethw_price_temp['result']['price'])
except Exception:
    ethw_price = 0
try:
    ethw_diff = int(ethw_diff_temp['nodes'][0]['difficulty'])
except Exception:
    ethw_diff = 0
ethw_block_time = 13
ethw_block_reward = 2

# Reward calculations


def reward_calc(price, diff, block_time, block_reward, hashrate, power, power_rate):
    if price != 0 and diff != 0 and block_time != 0:
        HR_req = diff/block_time
        est_revenue_th = (block_reward*(seconds_a_day/block_time))/HR_req
        est_revenue = ((hashrate*megahash))*est_revenue_th
        est_revenue_usd = est_revenue * price
        cost = (power/1000)*24*(power_rate)
        est_reward = est_revenue_usd - cost
        return est_reward
    else:
        est_reward = 0
        return est_reward


cfx_est_reward = reward_calc(price=cfx_price, diff=cfx_diff, block_time=cfx_block_time, block_reward=cfx_block_reward,hashrate=config['cfx']['hash'],power=config['cfx']['power'], power_rate=power_rate)
flux_est_reward = reward_calc(price=flux_price, diff=flux_diff*10000, block_time=flux_block_time, block_reward=flux_block_reward*config['flux_PA_multiplier'],hashrate=config['flux']['hash']/megahash,power=config['flux']['power'], power_rate=power_rate)
erg_est_reward = reward_calc(price=erg_price, diff=erg_diff, block_time=erg_block_time, block_reward=erg_block_reward,hashrate=config['erg']['hash'],power=config['erg']['power'], power_rate=power_rate)
etc_est_reward = reward_calc(price=etc_price, diff=etc_diff, block_time=etc_block_time, block_reward=etc_block_reward,hashrate=config['etc']['hash'],power=config['etc']['power'], power_rate=power_rate)
rvn_est_reward = reward_calc(price=rvn_price, diff=rvn_diff*2**32, block_time=rvn_block_time, block_reward=rvn_block_reward,hashrate=config['rvn']['hash'],power=config['rvn']['power'], power_rate=power_rate)
firo_est_reward = reward_calc(price=firo_price, diff=firo_diff*2**32, block_time=firo_block_time, block_reward=firo_block_reward,hashrate=config['rvn']['hash'],power=config['rvn']['power'], power_rate=power_rate)
ethw_est_reward = reward_calc(price=ethw_price, diff=ethw_diff, block_time=ethw_block_time, block_reward=ethw_block_reward,hashrate=config['ethw']['hash'],power=config['ethw']['power'], power_rate=power_rate)

 
print('CFX:  ', round(cfx_est_reward,2))
print('FLUX: ',round(flux_est_reward,2))
print('ERG:  ', round(erg_est_reward,2))
print('ETC:  ', round(etc_est_reward,2))
print('RVN:  ', round(rvn_est_reward,2))
print('FIRO:  ', round(firo_est_reward,2))
print('ETHW:  ', round(ethw_est_reward,2))

