#9.4 Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.
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
print(bigmail, bigcount)