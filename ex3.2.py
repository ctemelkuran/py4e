#Write a program to prompt for a score between 0.0 and 1.0.
#If the score is out of range, print an error. If the score is between 0.0 and 1.0
score = input("Enter score:")
try:
    scr = float(score)
except:
    print("Please enter a numerical value!")
    quit()
if scr < 0 or scr > 1:
    print("Out of range!")
elif scr>=0.9:
    print("A")
elif scr>=0.8:
    print("B")
elif scr>=0.7:
    print("C")
elif scr>=0.6:
    print("D")
else:
    print("F")
