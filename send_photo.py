import requests
from settings import TOKEN

url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

params = {
    "chat_id": 6567130987,
    "photo": "https://images.app.goo.gl/caVvKfYMw5mBjLBv7"

}

r = requests.get(url=url, params=params)
print(r.status_code)
