# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
#
# Minimum Number of Platforms Required for a Railway/Bus Station
# Given arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits.
# We are given two arrays which represent arrival and departure times of trains that stop.
#
# Examples:
#
# Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
# dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
# Output: 3
# Explantion: There are at-most three trains at a time (time between 11:00 to 11:20)
#
# Input: arr[] = {9:00, 9:40}
# dep[] = {9:10, 12:00}
# Output: 1
# Explantion: Only one platform is needed



#My own solution:


def timeStringToTime(timestring):
    hour=int(str(timestring).split(":")[0])
    min=int(str(timestring).split(":")[1])

    return (hour*60+min)


array1=['9:00', '9:40', '9:50', '11:00', '15:00', '18:00']
array2=['9:10', '12:00', '11:20', '11:30', '19:00', '20:00']

# array1=['9:00', '9:40']
# array2=['9:10', '12:00']

currentTrains=0
maxP=0

for i in range(len(array1)):
    array1[i]=timeStringToTime(array1[i])
    array2[i]=timeStringToTime(array2[i])


print(array1)
print(array2)


start=array1[0]
end=array2[len(array2)-1]

for i in range(start, end+1):

    if i in array1:
        print("Train arrrived")
        currentTrains+=1
    if i in array2:
        print("Train departed")
        currentTrains-=1
    if currentTrains>maxP:
        maxP=currentTrains

print(maxP)






#Solution from GeeksForGeeks, i know mine was crap:

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n=len(arr)
arr.sort()
dep.sort()

result=1
platforms=0;

i=0
j=0

while (i<n and j<n) :

    if arr[i]<=dep[j]:
        platforms+=1
        i+=1
    else:
        platforms-=1
        j+=1

    result=max(result,platforms)

print(result)






















