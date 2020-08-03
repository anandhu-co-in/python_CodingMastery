# https://www.geeksforgeeks.org/amazon-interview-experience-sde-1-amazon-wow-2020/?ref=leftbar-rightbar2.
# Given a string find the count of unique palindromic substrings
# Ex: aabaaa
#
# o/p: 6 ( a, b, aa, aba, aabaa, aaa)

#Not sure if this is a HORRIBLE SOLUTION, But it works!!

def printPalindromes(a):

    result=[]

    for i in range(len(a)):
        k=i
        c=a[k]
        temp=''
        while(k<len(a) and a[k]==c):
            temp = temp+a[k]

            #To handle even palindrome
            if(len(temp)==2):
                j = 1
                temp2 = temp
                while (True):
                    if i - j < 0 or i + 1 + j == len(a) or a[i - j] != a[i + 1+j]:
                        break
                    temp2 = a[i- j] + temp2 + a[i+1 + j]
                    if temp2 not in result:
                        result.append(temp2)
                    j = j + 1

            if temp not in result:
                result.append(temp)
            k=k+1
        j=1


        #Find all odd palindromes
        temp=a[i]
        while(True):
            if i-j<0 or i+j==len(a) or a[i-j] != a[i+j]:
                break
            temp=a[i-j]+temp+a[i+j]
            if temp not in result:
                result.append(temp)
            j=j+1


    print(sorted(result))
    print("{} unique palindromes!".format(len(result)))

a="abcddcba"

printPalindromes(a)
