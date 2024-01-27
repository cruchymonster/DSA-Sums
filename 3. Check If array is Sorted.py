def sort(num, n):
    for i in range(n):
        if num[i] <= num[i-1]:
            print("False")
            break
    print("True")


nums = [3, 4, 6, 7]
n = len(nums)
sort(nums, n)
