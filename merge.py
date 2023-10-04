def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    for j in range(n):
        nums1.append(nums2[j])
    nums1.sort()
    print(nums1)

merge([1,2,3],3,[4,5,6,2,3,1],6)