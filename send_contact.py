from pprint import pprint
import requests
from settings import TOKEN


url = f"https://api.telegram.org/bot{TOKEN}/sendContact"

params = {
    "chat_id":  6567130987,
    "phone_number": "+99812345678",
    "first_name":"Lisa"

}
r = requests.get(url=url, params=params)
print(r.status_code)
pprint(r.json())

