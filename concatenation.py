def getConcatenation(nums: list[int]) -> list[int]:
    ans = []
    j = len(nums)
    print(j)
    for i in range(2*j):
        if i<j:
            ans.append(nums[i])
            
        else:
            ans.append(nums[i-j])

    print(ans)


getConcatenation([1,2,1])                

