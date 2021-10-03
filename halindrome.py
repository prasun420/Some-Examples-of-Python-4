s="aaba"
length_s=len(s)
#print(s[-1])
if length_s%2==0:
    mid=int(length_s/2)
    s1=s[0:mid]
    s2=s[mid:]
    #print(s1)
    #print(s2)
    if (s1[::-1]==s1) or (s2[::-1]==s2) or (s[::-1]==s):
        print("This is a Halindrome")
    else:
        print("NO")

elif length_s%2!=0:
    if s[::-1]==s:
        print("this is halindrome")