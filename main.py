import os
from flask import Flask
import json
from bs4 import BeautifulSoup
import requests

# @app.route("/", method=['GET', 'POST'])
def lambda_function(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    print(page.status_code)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'lxml')
        out_of_stock_divs = soup.find('div', class_='sc-pc-channel-add-to-cart').text.strip(
            'Add to list')  # <--- change "text" to div
        print(out_of_stock_divs)
        if out_of_stock_divs == 'Out of stock':
            return json.dumps({
                "status": page.status_code,
                "in_stock": False}
            )
        else:
            return json.dumps({
                "status": page.status_code,
                "in_stock": True})
    else:
        return json.dumps({
            "status": page.status_code,
            "in_stock": False}
        )

#print(data_scraping('https://www.samsclub.com/p/5-tier-chrome-shelf-60-x24-x72/prod8250050?xid=plp_product_22'))
# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))