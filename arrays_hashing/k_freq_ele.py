def k_freq_ele(arr,k):
        list1 = []
        dict1 = {}
        for i in arr:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        dict1 = dict(sorted(dict1.items(),key = lambda item :item[1] , reverse = True))
        list2 = list(dict1.keys())
        x =0 
        while k>0:
                 list1.append(list2[x])
                 x = x+1
                 k = k-1
        return list1
print(k_freq_ele([1,1,1,2,2,3,4,4,4,4],2))

# TC - O(nlogn)
# SC - O(n)