import re

name=input("Enter file:")
handle = open(name)
sum=0
count=0
numbers=list()
for line in handle:
    line.rstrip()
    number=re.findall('[0-9]+',line)

    for num in number:
        count=count+1
        sum=sum+ int(num)

print("There are ",count,"values with sum=",sum)
