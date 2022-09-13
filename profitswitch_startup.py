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
                  'diff': 'https://api.minerstat.com/v2/coins?list=FIRO'}
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

print(cfx_diff_temp['data']['list'][0]['difficulty'])

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

if cfx_price != 0 and cfx_diff != 0 and cfx_block_time != 0:
    HR_req_cfx = cfx_diff/cfx_block_time
    cfx_est_revenue_th = (cfx_block_reward*(seconds_a_day/cfx_block_time))/HR_req_cfx
    cfx_est_revenue = ((config['cfx']['hash']*megahash))*cfx_est_revenue_th
    cfx_est_revenue_usd = cfx_est_revenue * cfx_price
    cfx_cost = (config['cfx']['power']/1000)*24*(power_rate)
    cfx_est_reward = cfx_est_revenue_usd - cfx_cost
else:
    cfx_est_reward = 0

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
    etc_est_revenue = ((config['etc']['hash']*megahash))*etc_est_revenue_th
    etc_est_revenue_usd = etc_est_revenue * etc_price
    etc_cost = (config['etc']['power']/1000)*24*(power_rate)
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
    new_algo = 'Better off not mining'
try:
    os.system('systemctl --user start profitswitch.service')
except Exception as e:
    print(e)
