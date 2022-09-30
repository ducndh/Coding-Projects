from datetime import date
import pandas as pd
import time
import requests
import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('config')
connection = psycopg2.connect(
    host=config['config']['host'],
    database=config['config']['clickstream'],
    user=config['config']['user'],
    password=config['config']['password'],
)
connection.autocommit = True
#print date to help users to track down when the file was generated.
data = date.today()

@app.post("/load_data")
async def load_item_data_shopee():
    try:
        url_api_request = 'https://shopee.com.br/api/v4/recommend/recommend?bundle=shop_page_product_tab_main&limit=999&offset=0&section=shop_page_product_tab_main_sec&shopid=' + seller_shopee_id
        r = requests.get(url_api_request)
        ads = r.json()['data']['sections'][0]['data']['item']
        file = pd.to_csv(ads, delimiter='\t', header=[], nrows = len(ads))
        cursor = connection.cursos()
        cursor.copy_from(file, 'shopee')
    except Exception as e:
        cursor.close()
        return {'result': e}