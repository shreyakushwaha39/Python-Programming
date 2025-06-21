#WAP to count the number of vowels in a given string.
def count_vowel(s):
    count=0
    for i in s:
        if(i in 'aeiouAEIOU'):
            count+=1
    return count
n=input("enter a string: ")
ans=count_vowel(n)
print("number of vowel in a given string is ",ans)

