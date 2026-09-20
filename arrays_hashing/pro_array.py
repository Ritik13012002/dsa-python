# PRODUCT OF ARRAY EXCEPT SELF
# Given an integer array nums, return an array answer such that answer[i] is equal to
# the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
def product_except_self(nums):
    n = len(nums)
    output = [1] * n
    prefix =1 
    for i in range(n):
        output[i] = prefix 
        prefix *= nums[i]
    suffix =1 
    for i in range(n-1 , -1 ,-1):
        output[i] *= suffix
        suffix *= nums[i]
    return output

print(product_except_self([1,2,3,4]))
print(product_except_self([-1,1,0,-3,3]))