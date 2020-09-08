# Given A String, you need to find the Largest Palindromic Substring inside it

def find_largest_palindrome(str):
    largest_pal = ""
    n = len(str)

    def expand(pointer1, pointer2):
        while pointer1 - 1 >= 0 and pointer2 + 1 < n:

            if str[pointer1 - 1] == str[pointer2 + 1]:
                pointer1 = pointer1 - 1
                pointer2 = pointer2 + 1
                continue
            break
        return str[pointer1:pointer2 + 1]

    for i in range(0, n):
        pal = expand(i, i)
        if len(pal) > len(largest_pal):
            print("Found new large pal {} with leng {}".format(pal, len(pal)))
            largest_pal = pal

        if i < len(str) - 1 and str[i] == str[i + 1]:
            pal = expand(i, i + 1)
            if len(pal) > len(largest_pal):
                print("Found new pal {} with length {}, its an even pal".format(pal, len(pal)))
                largest_pal = pal

    return largest_pal


print(find_largest_palindrome("malayalamXaaaaaOOaaaaaX"))

# There is a better approch called manachers algorithm which has O(N),, Above one has O(n2)
# https://www.youtube.com/watch?v=nbTSfrEfo6M
