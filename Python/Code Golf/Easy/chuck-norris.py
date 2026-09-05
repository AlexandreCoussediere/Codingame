from itertools import groupby
m=input()
b="".join(format(ord(c),'07b')for c in m)
print(" ".join(("0"if k=="1"else"00")+" "+"0"*len(list(g))for k,g in groupby(b)))
