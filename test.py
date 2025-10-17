def update_pos(ls1,ls2):
    res = [0,0]
    # check len
    if len(ls1)!=len(ls2):
        return None
    else:
        for i, n in enumerate(ls1):
            res[i] = n+ls2[i]
    
    return res


print(update_pos([-5,22],[1,100]))