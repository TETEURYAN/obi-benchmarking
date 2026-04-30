a=int(input())
b=int(input())
cadeiras=[0,1,2]
ana=(1+b-1)%3
if cadeiras[ana]==0:
    beatriz=(1+b-1)%3
else:
    beatriz=(1+b)%3
for i in range(3):
    if cadeiras[i]!=0 and cadeiras[i]!=cadeiras[ana] and cadeiras[i]!=cadeiras[beatriz]:
        print(cadeiras[i])