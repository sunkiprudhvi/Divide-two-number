def div_ab(a,b):
    if b==0:
        return none
    q=a//b
    r=a%b
    if r ==0:
        return q
    res=[str(q),'.']
    rem_map={}
    while r !=0:
        if r in rem_map:
            res.insert(rem_map[r],'(')
            res.append(")")
            return "".join(res)
        rem_map[r]=len(res)
        r=r*10
        q=r//b
        res.append(str(q))
        r=r%b
    return "".join(res)
a=(int(input("enter a value : ")))
b=(int(input("enter b value : ")))
ans=div_ab(a,b)
print("ans : ",ans)
