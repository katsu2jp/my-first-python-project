import requests
response = requests.get("https://google.com")
print("ステータスコード：", response.status_code)