def Count_even():
    count = 0
    with open("D:\Python- Apna College\python codes\lecture 7\practice2.txt","r") as f:
        data = f.read()
        nums = data.split(",")
        for val in nums:
            if(int(val))%2 == 0:
                count += 1
    return print(count)
Count_even()