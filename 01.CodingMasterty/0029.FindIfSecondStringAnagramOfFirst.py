#Write a program to check if the second string is anagram of the first
#Anagram means a word formed by rearranging letters of another word
#https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/


#Python key in dic has O(N) complexity but dic.get(key) has O(1) complexity!
#Refer this url for complexities https://www.geeksforgeeks.org/complexity-cheat-sheet-for-python-operations/


def validAnagram(string1,string2):
    dict = {}

    if len(string1)!=len(string2):
        return False

    for x in string1:
        if dict.get(x) is None:
            dict[x]=1
        else:
            dict[x]=dict[x]+1

    for x in string2 :
        if dict.get(x) is None or dict[x]==0:
            return False
        else:
            dict[x]=dict[x]-1
    return True
    pass





print(validAnagram('','')) #true
print(validAnagram('aaz','zza')) #false
print(validAnagram('anagram','nagaram')) #true
print(validAnagram('anagram','nagaramaa')) #true
print(validAnagram('aabcdefyj','fabcydeaj'))#true
