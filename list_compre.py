name = "mbox-short.txt"
#name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mails = {}

for line in handle:
    if not line.startswith('From:'): continue
    pieces = line.split()
    for piece in pieces:
        if piece == pieces[1]:
            mails[piece] = mails.get(piece, 0) + 1

#counts the biggest item
bigcount = None
bigmail= None
for k,v in mails.items():
    if bigcount is None or v > bigcount:
        bigcount = v
        bigmail = k
#print(bigmail, bigcount)

#sorts the items and prints first 5
sort = sorted( [ (v, k) for k, v in mails.items() ], reverse=True )
for v, k in sort[:5] :
    print(k, v)