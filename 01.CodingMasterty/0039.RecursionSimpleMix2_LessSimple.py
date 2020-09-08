# Accept a string and returns new string in reverse
def reverse(str):
    if len(str) <= 1: return str
    return str[-1] + reverse(str[0:-1])


# Check if given string is palindrome
def isPalidrome(str):
    if len(str) <= 1: return True
    return str[0] == str[-1] and isPalidrome(str[1:-1])


# Flatten nested arrays into one
def flatten(arr):
    answer = []
    for x in arr:
        if isinstance(x, list):  # using instance to check if x a list
            answer = answer + flatten(x)
        else:
            answer.append(x)
    return answer


# input and object and return array of strings in it
# Java script solution below
# collectStrings Solution: Pure Recursion Version
#
# function collectStrings(obj) {
#     var stringsArr = [];
#     for(var key in obj) {
#         if(typeof obj[key] === 'string') {
#             stringsArr.push(obj[key]);
#         }
#         else if(typeof obj[key] === 'object') {
#             stringsArr = stringsArr.concat(collectStrings(obj[key]));
#         }
#     }
#
#     return stringsArr;
# }


print(reverse("abcdef"))
print(isPalidrome("malayalam"))
print(flatten([1, 2, 3, 4, [5, 6, 7, [8, 9, 10, [[10.6]], [11]]]]))
