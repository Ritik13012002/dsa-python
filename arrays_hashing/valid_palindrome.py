def valid_palindrome(s):
     s = [c.lower() for c in s if c.isalnum()]
     first,last = 0 , len(s)-1
     while first < last:
        if s[first] != s[last]:
            return False
        first , last = first+1,last-1
     return True
print(valid_palindrome("A man, a plan, a canal: Panama"))

# TC - O(n)
# SC - O(n)