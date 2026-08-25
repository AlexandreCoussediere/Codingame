a,b,c,d=[int(i)for i in input().split()]
while 1:y=(d>b)-(d<b);x=(c>a)-(c<a);print(["S","","N"][y+1]+["E","","W"][x+1]);d-=y;c-=x
