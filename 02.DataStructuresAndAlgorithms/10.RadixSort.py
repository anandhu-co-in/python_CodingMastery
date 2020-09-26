# Implement Radix Sort
import math


# Helper function to get specific digit in a position
def getDigit(number, pos):
    digit = math.floor(number / pow(10, pos)) % 10
    # print("{} has {} in position {}".format(number,digit,pos))
    return digit


def digitCount(num):
    if num==0 : return 1
    count= math.floor(math.log10(num))+1;
    # print("{} has {} digits".format(num,count));
    return count

def mostDigits(nums):
    maxdigits=0
    for x in nums:
        maxdigits=max(digitCount(x),maxdigits)
    # print("Largest digit count is {}".format(maxdigits))
    return  maxdigits



def radixSort(arr):


    sorteArray = []

    iter=mostDigits(arr)
    for i in range(0,iter):
        buckets = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        print(buckets)
        # buckets = dict.fromkeys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], []) #<<--------------Intresting! If i use this code, it doesent work!
        # print(buckets)
        for x in arr:
            bucket=getDigit(x,i)

            if bucket in buckets:
                buckets[bucket].append(x)
            else:
                # print("Created bucket {}".format(buckets))
                buckets[bucket]=[x]

        sorteArray=[]
        print("Buckets : {}".format(buckets))
        for b in buckets:
            # print("Current key {}".format(b))
            sorteArray+=buckets[b]
        print("Sorted Merged Buckets : {}".format(sorteArray))
        arr=sorteArray


    return (sorteArray)

getDigit(1234,3)
digitCount(0)
# print(radixSort([124,5675,343,675,11,54,10,7,2]))
print(radixSort([3221,1,10,9680,577,9420,7,5622,4793,2030,3138,82,2599,743,4127]))



# Complexity=O(nk)




# function getDigit(num, i) {
#   return Math.floor(Math.abs(num) / Math.pow(10, i)) % 10;
# }
#
# function digitCount(num) {
#   if (num === 0) return 1;
#   return Math.floor(Math.log10(Math.abs(num))) + 1;
# }
#
# function mostDigits(nums) {
#   let maxDigits = 0;
#   for (let i = 0; i < nums.length; i++) {
#     maxDigits = Math.max(maxDigits, digitCount(nums[i]));
#   }
#   return maxDigits;
# }
#
# function radixSort(nums){
#     let maxDigitCount = mostDigits(nums);
#     for(let k = 0; k < maxDigitCount; k++){
#         let digitBuckets = Array.from({length: 10}, () => []);
#         for(let i = 0; i < nums.length; i++){
#             let digit = getDigit(nums[i],k);
#             digitBuckets[digit].push(nums[i]);
#         }
#         nums = [].concat(...digitBuckets);
#     }
#     return nums;
# }
#
# radixSort([23,345,5467,12,2345,9852])