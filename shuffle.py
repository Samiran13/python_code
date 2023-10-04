def shuffle(nums: list[int], n: int) -> list[int]:
    my_list = []
    
    my_list1 = nums[:n]
    my_list2 = nums[n:]
    #print(my_list2)
    for i in range(len(nums)):
        if i%2 ==0:
            my_list.append(my_list1[int(i/2)])
        else:
            my_list.append(my_list2[int((i-1)/2)])

    print(my_list)            



shuffle([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],10)    

