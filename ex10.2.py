name = "mbox-short.txt"
#name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time = {}

for line in handle:
    if not line.startswith('From'): continue
    pieces = line.split()
    for piece in pieces:
        if len(piece) == 8:
            time[piece[:2]] = time.get(piece[:2], 0) + 1

tmp = list()
tmp = (sorted( [ (k, v) for k, v in time.items() ]) )
for k, v in tmp:
    print(k, v)