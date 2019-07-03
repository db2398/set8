most=list(input())
if len(most)%2==0:
    most[int(len(most)/2)] ='*'
    most[int(len(most)/2)-1]='*'
else:
    most[int(len(most)/2)] ='*'
for i in range(0,len(most)):
    print(most[i],end='')
