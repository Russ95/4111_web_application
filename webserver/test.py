a='1234-11-23'
res=0
if a[4]=='-' and a[7]=='-':
    t=a.split('-')
    if len(t[0])==4 and len(t[1])==2 and len(t[2])==2:
        for value in t:
            try:
                val = int(value)
                res=1
            except ValueError:
 #               print("That's not an int!")
                res=2
    else:
        res=2
else:
    res=2
print (res)