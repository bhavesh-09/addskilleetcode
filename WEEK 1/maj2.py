def majorityElement(nums):     
    res = []
    m1=m2=(2**32)-1
    c1=c2=0
    for i in nums:
        if i==m1:
            c1+=1
        elif i==m2:
            c2+=1
        elif c1==0:
            m1=i
            c1=1
        elif c2==0:
            m2=i
            c2=1
        else :
            c1-=1
            c2-=1
    c1 =c2 =0
    for i in nums:
        if(m1==i):
            c1+=1
        elif(m2==i):
            c2+=1
            
    if(c1> len(nums)//3):
        res.append(m1)
    if(c2> len(nums)//3):
        res.append(m2)
    return res


a = [1,1,1,3,3,2,2,2]
print(majorityElement(a))