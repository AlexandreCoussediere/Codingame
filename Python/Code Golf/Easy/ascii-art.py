l,h,t=int(input()),int(input()),input()
A="ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
R=[input()for _ in range(h)]
p=[(A.index(c.upper())if c.upper()in A else 26)*l for c in t]
for row in R:print("".join(row[x:x+l]for x in p))
