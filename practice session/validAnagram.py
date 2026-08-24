# def is_anagram(s , t):
#     s = sorted(s)
#     t = sorted(t)
#     if s ==t:
#         return True
#     else:
#         return False
# print(is_anagram("peter","retrp"))

def is_anagram(s , t):
    if len(s) != len(t):
        return False
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in t:
        if i in dict:
            dict[i] -= 1
        else:
            return False
    for i in dict:
        if dict[i] != 0:
            return False
    return True
print(is_anagram("peter","retep"))
