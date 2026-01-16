n=int(input())
q=int(input())
for i in range(q):
    uputa,x=map(int,input().split())
    if uputa==1:
        n=n-x
    else:
        n=n//x
if n<=0:
    print("STOP")
    while True:
        a=input()
else:
    print(n)
