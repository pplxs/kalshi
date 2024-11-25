import os
from py_clob_client.constants import POLYGON
from py_clob_client.client import ClobClient
import numpy as np
import pandas as pd

from dotenv import load_dotenv

load_dotenv('keys.env')

host = "https://clob.polymarket.com"
key = os.getenv("api_passphrase")
chain_id = POLYGON

# Create CLOB client and get/set API credentials
client = ClobClient(host, key=key, chain_id=chain_id)

all_data = pd.DataFrame()

next_cursor = ''
while True:

    resp = client.get_markets(next_cursor=next_cursor)
    next_cursor = resp['next_cursor']
    print(next_cursor)
    # # 检查是否有下一页
    if next_cursor=='LTE=':
        break
    resp = client.get_markets(next_cursor='')
    data = pd.DataFrame(resp['data'])
    all_data = pd.concat([all_data, data], ignore_index=True)

all_data.reset_index(inplace=True, drop=True)
all_data.to_csv('all_data.csv',index=False)



