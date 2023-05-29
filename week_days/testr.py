import requests

t = requests.get('https://stihi.ru/poems/selected.html')
print(t.text)