name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counter=dict()
temp=list()
words=list()
for line in handle:
    line.rstrip()
    if line.startswith("From "):
        line=line.split()
        line=line[5].split(":")
        for hrs in line[0].split():
            counter[hrs]=counter.get(hrs,0)+1

print(counter)

for k,v in sorted(counter.items()):
    print(k,v)
