# def reverse(str):
#     return str[::-1]

# print(reverse("peter"))

def reversei(s):
    if len(s)>1:
        i = 0
        j = len(s)-1
        s = list(s)
        while i<j:
            s[i],s[j]=s[j],s[i]
            i = i+1
            j = j-1
        return "".join(s)
    else:
        return s

print(reversei("peter"))