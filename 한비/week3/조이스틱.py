
#65~90 A~Z ord써줄것

name ="JEROEN" #56번 나와야함
#vs_first
first=ord('A')#65
last=ord('Z')#90

name_li=list(name)
first_li=['A' for _ in range(len(name_li))]
#조이스틱

#각각의 스틱들 카운트

total=0
stick=0 #전체 횟수
cursor=0
#일반적인경우
for i in range(len(name_li)):
    value=ord(name_li[i])
    sub1 = value-first
    sub2 = last-value
    
    if sub1<=sub2:
        stick=stick+sub1 
        print(sub1)
    else : 
        stick=stick+sub2
        print(sub2)
total=total+stick+len(name_li)-1


    
print(total)
