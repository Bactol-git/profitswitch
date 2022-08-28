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

    
urls = [{'algo': 'eth', 'price': 'https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=ETHUSDT',
                  'diff': 'https://api.minerstat.com/v2/coins?list=ETH',
                  'block_time': 'https://whattomine.com/coins/151.json?hr=244.0&p=1040.0&fee=0.0&cost=0.1&cost_currency=USD&hcost=0.0&span_br=1h&span_d=24'},
                 {'algo': 'flux', 'price':'https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=FLUXUSDT',
                  'diff': 'https://api.runonflux.io/daemon/getmininginfo'},
                  {'algo': 'erg', 'price': 'https://www.coingecko.com/price_charts/2484/usd/24_hours.json',
                  'diff': 'https://api.ergoplatform.com/blocks?limit=1&offset=0&sortBy=height&sortDirection=desc'},
                 {'algo': 'etc', 'price': 'https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=ETCUSDT',
                  'diff': 'https://api.minerstat.com/v2/coins?list=ETC'},
                 {'algo': 'rvn', 'price': 'https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=RVNUSDT',
                  'diff': 'https://explorer.mangofarmassets.com/api/status?q=getInfo'},
                 {'algo': 'firo', 'price': 'https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-product-by-symbol?symbol=FIROUSDT',
                  'diff': 'https://api.minerstat.com/v2/coins?list=FIRO'}
                 ]



eth_price_temp = api_fetch(urls[0]['price'])
eth_diff_temp = api_fetch(urls[0]['diff'])
eth_block_time_temp = api_fetch(urls[0]['block_time'])
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


try:
    eth_price = float(eth_price_temp['data']['c'])
except Exception as e:
    print(e)
    eth_price = 0
try:
    eth_diff = int(eth_diff_temp[0]['difficulty'])
except Exception:
    eth_diff = 0
try:
    eth_block_time = float(eth_block_time_temp['block_time'])
except Exception:
    eth_block_time = 0
eth_block_reward = 2

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
erg_block_reward = 48

try:
    etc_price = float(etc_price_temp['data']['c'])
except Exception:
    etc_price = 0
try:
    etc_diff = int(etc_diff_temp[0]['difficulty'])
except Exception:
    etc_diff = 0
etc_block_time = 13
etc_block_reward = 2.48

try:
    rvn_price = float(rvn_price_temp['data']['c'])
except Exception:
    rvn_price = 0
try:
    rvn_diff = int(rvn_diff_temp['info']['difficulty'])
except Exception:
    rvn_diff = 0
rvn_block_time = 60
rvn_block_reward = 2500

try:
    firo_price = float(firo_price_temp['data']['c'])
except Exception:
    firo_price = 0
try:
    firo_diff = int(firo_diff_temp[0]['difficulty'])
except Exception:
    firo_diff = 0
firo_block_time = 150
firo_block_reward = 1.5625


# Reward calculations

if eth_price != 0 and eth_diff != 0 and eth_block_time != 0:
    HR_req_eth = eth_diff/eth_block_time
    eth_est_revenue_th = (eth_block_reward*(seconds_a_day/eth_block_time))/HR_req_eth
    eth_est_revenue = ((config['eth']['hash']*megahash))*eth_est_revenue_th
    eth_est_revenue_usd = eth_est_revenue * eth_price
    eth_cost = (config['eth']['power']/1000)*24*(power_rate)
    eth_est_reward = eth_est_revenue_usd - eth_cost
else:
    eth_est_reward = 0

if flux_price != 0 and flux_diff != 0:
    HR_req_flux = flux_diff*10000/flux_block_time
    flux_est_revenue_th = (flux_block_reward*config['flux_PA_multiplier']*(seconds_a_day/flux_block_time))/HR_req_flux
    flux_est_revenue = ((config['flux']['hash']))*flux_est_revenue_th
    flux_est_revenue_usd = flux_est_revenue * flux_price
    flux_cost = (config['flux']['power']/1000)*24*(power_rate)
    flux_est_reward = flux_est_revenue_usd - flux_cost
else:
    flux_est_reward = 0

if erg_price != 0 and erg_diff != 0:
    HR_req_erg = erg_diff/erg_block_time
    erg_est_revenue_th = (erg_block_reward*(seconds_a_day/erg_block_time))/HR_req_erg
    erg_est_revenue = ((config['erg']['hash']*megahash))*erg_est_revenue_th
    erg_est_revenue_usd = erg_est_revenue * erg_price
    erg_cost = (config['erg']['power']/1000)*24*(power_rate)
    erg_est_reward = erg_est_revenue_usd - erg_cost
else:
    erg_est_reward = 0

if etc_price != 0 and etc_diff != 0:
    HR_req_etc = etc_diff/etc_block_time
    etc_est_revenue_th = (etc_block_reward*(seconds_a_day/etc_block_time))/HR_req_etc
    etc_est_revenue = ((config['eth']['hash']*megahash))*etc_est_revenue_th
    etc_est_revenue_usd = etc_est_revenue * etc_price
    etc_cost = (config['eth']['power']/1000)*24*(power_rate)
    etc_est_reward = etc_est_revenue_usd - etc_cost
else:
    etc_est_reward = 0

if rvn_price != 0 and rvn_diff != 0:
    HR_req_rvn = (rvn_diff*2**32)/rvn_block_time
    rvn_est_revenue_th = (rvn_block_reward*(seconds_a_day/rvn_block_time))/HR_req_rvn
    rvn_est_revenue = ((config['rvn']['hash']*megahash))*rvn_est_revenue_th
    rvn_est_revenue_usd = rvn_est_revenue * rvn_price
    rvn_cost = (config['rvn']['power']/1000)*24*(power_rate)
    rvn_est_reward = rvn_est_revenue_usd - rvn_cost
else:
    rvn_est_reward = 0

if firo_price != 0 and firo_diff != 0:
    HR_req_firo = (firo_diff*2**32)/firo_block_time
    firo_est_revenue_th = (firo_block_reward*(seconds_a_day/firo_block_time))/HR_req_firo
    firo_est_revenue = ((config['rvn']['hash']*megahash))*firo_est_revenue_th
    firo_est_revenue_usd = firo_est_revenue * firo_price
    firo_cost = (config['rvn']['power']/1000)*24*(power_rate)
    firo_est_reward = firo_est_revenue_usd - firo_cost
else:
    firo_est_reward = 0

    
print('ETH:  ', round(eth_est_reward,2))
print('FLUX: ',round(flux_est_reward,2))
print('ERG:  ', round(erg_est_reward,2))
print('ETC:  ', round(etc_est_reward,2))
print('RVN:  ', round(rvn_est_reward,2))
print('FIRO:  ', round(firo_est_reward,2))
