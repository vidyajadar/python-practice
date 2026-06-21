S = "1998"
l=any (c.isalpha() for c in S)
n=any (c.isdigit() for c in S)
if l and n:
    print(True)
else:
    print(False)