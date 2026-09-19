# def group_anagrram(s):
#     anagram = {}
#     for i in s:
#         key = ''.join(sorted(i))
#         anagram.setdefault(key, []).append(i)
#     return list(anagram.values()) 

def group_anagram(s):
    anagram={}
    for i in s:
        count = [0] * 26
        for j in i:
            count[ord(j) - ord('a')] +=1
        key = tuple(count)
        anagram.setdefault(key , []).append(i)
    return list(anagram.values())

print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))

# TC - O(nk) where n is the number of strings and k is the maximum length of a string
# SC - O(nk) where n is the number of strings and k is the maximum length of a string
