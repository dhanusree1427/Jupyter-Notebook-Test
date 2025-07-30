def evenodd(n):
    if(n%2==0):
        print('even')
    else:
        print('odd')
n = int(input())

def palindrome(s):
    if(s==s[::-1]):
        print('palindrome')
    else:
        print('not palindrome')
s = input()