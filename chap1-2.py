import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)

response.encoding = response.apparent_encoding

filename = "download.txt"
f = open(filename, mode="w")

f.write(response.text)

f.close

