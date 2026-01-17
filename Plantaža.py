n=int(input())
prvo=0
for i in range(n):
    Ji=int(input())
    prvo+=Ji
print(prvo)
drugo=prvo//100
print(drugo)
if prvo%100==0:
    print(0)
else:
    trece=100-(prvo%100)
    print(trece)
