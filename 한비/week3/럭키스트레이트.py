n=input()

if len(n)%2==0:
    half=int(len(n)//2)
    
    li1 = list(map(int, list(n[:half])))
    li2 = list(map(int, list(n[half:])))  
    
    if sum(li1) == sum(li2):
        print("LUCKY")
    else:
        print("READY")