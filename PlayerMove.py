def Move(dir):
    if(up.value()==0):
        if(dir=="down"):
            return dir
        else:
            return "up"
    elif(down.value()==0):
        if(dir=="up"):
            return dir
        else:
            return "down"
    elif(left.value()==0):
        if(dir=="right"):
            return dir
        else:
            return "left"
    elif(right.value()==0):
        if(dir=="left"):
            return dir
        else:
            return "right"
    else:
        return dir

def Snake(dir, sn):
    u=(56,57,58,59,60,61,62,63)
    r=(0,8,16,24,32,40,48,56)
    l=(7,15,23,31,39,47,55,63)
    d=(0,1,2,3,4,5,6,7)
    relat=(63,15,31,47,63,79,95,111)
    
    if(dir=="up"):
        for t in range(8):
            if(sn>= r[t-1] and sn<= l[t-1]):
                return relat[t]-sn
            
    elif(dir=="down"):
        for t in range(8):
            if(sn>=r[t-1] and sn<=l[t-1]):
                return relat[t-1]-sn
            
    elif(dir=="right"):
        for t in range(8):
            if(sn>=r[t-1] and sn<=l[t-1]):
                print(t%2)
                if(t%2==0):
                    for t in range(8):
                        if(sn==r[t]):
                            return l[t]
                    return sn-1
                else:
                    for t in range(8):
                        if(sn==l[t]):
                            return r[t]
                    return sn+1                    
    
    elif(dir=="left"):
        for t in range(8):
            if(sn>=r[t-1] and sn<=l[t-1]):
                print(t%2)
                if(t%2==0):
                    for t in range(8):
                        if(sn==l[t]):
                            return r[t]
                    return sn+1
                else:
                    for t in range(8):
                        if(sn==r[t]):
                            return l[t]
                    return sn-1 
    
    else:
        return sn