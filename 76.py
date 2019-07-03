y8=int(input())
if(y8>1):
   for i in range (2,y8):
      if(y8%i==0):
       print("yes")
       break
   else:
      print("no")
