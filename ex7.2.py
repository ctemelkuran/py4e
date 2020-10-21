# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
toplam = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    fs = line.rstrip()
    count = count + 1
    numpos = fs.find(':')
    num = fs[numpos+2:]
    if num.startswith("0"):
      toplam = toplam + float(num)

print("Average spam confidence:", toplam/count)
