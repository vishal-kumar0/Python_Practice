# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count=0
sum=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
         continue
    line.rstrip()
    count=count+1
    pos=line.find(' ')
    num=line[pos+1:]
    sum=float(num)+sum

print("Average spam confidence:", (sum/count))
