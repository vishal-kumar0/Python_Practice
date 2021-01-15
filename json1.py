import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter url:")
print("Retriving", url)
html = urllib.request.urlopen(url).read()

sum=0

info = json.loads(html)
print("Count :", len(info))

for item in info['comments']:
    sum = sum + item['count']

print("Sum", sum)
