# Given a string, determine if there's a way 
# to arrange the string such that the string is a palindrome. 
# If such arrangement exists return a palindrome else return None

def make_palindrome(string):
    count={}
    odd_char =""
    palindrome = ''
    for s in string:
        if s not in count:
            count[s] =1
        else:
            count[s]+=1
    print(count)
    for c,cnt in count.items():
        if cnt %2 ==0:
            palindrome += c*(cnt//2)
        elif not odd_char:
            odd_char=c
            palindrome += c*(cnt//2)
        else:
            return None
    
    return palindrome + odd_char + palindrome[::-1]

print(make_palindrome("moomma"))