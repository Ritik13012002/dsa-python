import string
def wordfreq(s):
    s = s.lower()
    s = s.translate(str.maketrans("","",string.punctuation))
    s = s.split()
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] =1 
    return sorted(dict.items(), key = lambda x: (x[1],x[0]),reverse = True)


print(wordfreq("My ,name is Peter Parker and Peter Parker is spiderman? Spiderman is the member of Avengers and His girfriend name is MJ"))