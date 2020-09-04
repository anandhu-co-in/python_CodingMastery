# Need a function which will find if the charectors of one array is present in the second array, in same order

# I came up with this recursive solution, i think i needd to get better with array slicing so i can make this code
# better
def checkIfSubSequence(array1, array2, pos1=0, pos2=0):
    global steps
    if pos1 == len(array1):
        return True
    i = pos1
    j = pos2
    while i < len(array1):
        while j < len(array2):
            if array1[i] == array2[j] and checkIfSubSequence(array1, array2, i + 1, j + 1):
                return True
            j = j + 1
        i = i + 1
    return False


# Test
print(checkIfSubSequence("hello", "dude hello world"))  # true
print(checkIfSubSequence("sing", "sting"))  # true
print(checkIfSubSequence("abc", "abracadabra"))  # true
print(checkIfSubSequence("abc", "acd"))  # False
print(checkIfSubSequence("abc", "cab"))  # False

# isSubsequence Solution - Iterative
# function isSubsequence(str1, str2) {
#   var i = 0;
#   var j = 0;
#   if (!str1) return true;
#   while (j < str2.length) {
#     if (str2[j] === str1[i]) i++;
#     if (i === str1.length) return true;
#     j++;
#   }
#   return false;
# }

# Javascrpt version similar to the recursive solution i implemented above. but using slices operation
# isSubsequence Solution - Recursive but not O(1) Space
# function isSubsequence(str1, str2) {
#   if(str1.length === 0) return true
#   if(str2.length === 0) return false
#   if(str2[0] === str1[0]) return isSubsequence(str1.slice(1), str2.slice(1))
#   return isSubsequence(str1, str2.slice(1))
# }
