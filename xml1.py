import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter URL: ')
print("Retriving", url)
html = urllib.request.urlopen(url).read()
count = 0
sum=0


tree = ET.fromstring(html)

results = tree.findall('comments/comment')
print('Count:', len(results))

for item in results:
    sum = sum + int(item.find('count').text)
    count = count+1

print("Sum:", sum)
print("Count", count)
