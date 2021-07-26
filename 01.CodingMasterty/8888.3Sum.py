

def threeSum(nums):

    nums.sort()
    ans = []

    for i in range(len(nums) - 2):

        tempSum = (0 - nums[i])

        p1 = i + 1
        p2 = len(nums) - 1

        while (p1 < p2):

            if nums[p1] + nums[p2] == tempSum:
                ans.append([nums[i], nums[p1], nums[p2]])

                while (p1 < p2 and nums[p1 + 1] == nums[p1]):
                    p1 = p1 + 1
                while (p1 < p2 and nums[p2 - 1] == nums[p2]):
                    p2 = p2 - 1

                p1+=1
                p2-=1

            elif nums[p1] + nums[p2] < tempSum:
                p1 += 1
            else:
                p2 -= 1

    print(ans)

threeSum([-1,0,1,2,-1,-4])


def threeSum2(nums):
    nums.sort()
    ans = []

    for i in range(len(nums) - 2):

        tempSum = (0 - nums[i])

        p1 = i + 1
        p2 = len(nums) - 1

        while (p1 < p2):

            if nums[p1] + nums[p2] == tempSum:
                ans.append([nums[i], nums[p1], nums[p2]])

                p1 += 1
                p2 -= 1

                while (p1 < p2 and nums[p1 + 1] == nums[p1]):
                    p1 = p1 + 1
                while (p1 < p2 and nums[p2 - 1] == nums[p2]):
                    p2 = p2 - 1
            elif nums[p1] + nums[p2] < tempSum:
                p1 += 1
            else:
                p2 -= 1

    print(ans)


threeSum2([-1,0,1,2,-1,-4])



