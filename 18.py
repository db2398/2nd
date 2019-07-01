check,valid=map(int,input().split())
for i in range(check+1,valid):
 final=i
 find=0
while(i>0):
 dot=i%10
 find=find+(dot**3)
 i=i//10
 if(find==final):
  print(find,end=" ")
