def cal_fact(f):
    if f==1 or f==0 :
        return 1
    else:
        return f* cal_fact(f-1)

print(cal_fact(4))