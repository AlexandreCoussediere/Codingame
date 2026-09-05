n,w,r,x,y,c,z,v=[int(i)for i in input().split()]
e={}
for i in range(v):f,p=[int(j)for j in input().split()];e[f]=p
while True:
 l=input().split();o=int(l[0]);q=int(l[1]);d=l[2]
 if o==-1 or e.get(o)==q:print("WAIT");continue
 t=y if o==x else e.get(o)
 m=t is not None and((d=="RIGHT"and q>=t)or(d=="LEFT"and q<=t))
 u=q+1 if d=="RIGHT" else q-1
 print("BLOCK" if m or u<0 or u>=w else "WAIT")
