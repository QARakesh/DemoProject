x=(1,2,3,4,5,6,7,8,9)
count_odd=0
count_even=0
for i in x:
    if i%2==0:
        count_odd+=1
    else:
        count_even+=1
print("Even number is :- ",count_even)
print("Odd Number is :-",count_odd)

n=5
for i in range(n):
    for j in range(i):
        print(" * ",end=' ')
    print(' ')
for i in range(n,0,-1):
    for j  in range(i):
        print(" * ",end=' ')
    print(' ')


n=7
for i in range(n,0,-1):
    for j in range(i):
        print(" # ",end=' ')
    print(' ')
for i in range(n+1):
    for j in range(i):
        print(" # ",end=' ')
    print(' ')

class election():
    def __init__(self,name,winner)
	    self.name=name
		self.winner=winner
e=(election.name="Lokh Sabha",election.winner="Narendra Modi")
print(election)

        




