ff=str(input())
g=list(ss)
u=len(ss)
h=""
if u%2==0:
  d[int(u/2)]="*"
  d[int(u/2-1)]="*"
else:
   g[int(u/2)]="*"
h=h.join(g)
print(h)
