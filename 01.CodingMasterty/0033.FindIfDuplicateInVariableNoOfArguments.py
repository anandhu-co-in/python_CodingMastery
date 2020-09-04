# In python we use *args to pass variable no of arguments.
# f you also write other arguments before *args, that will be taken first and the remaining ones will be added in *args


def findIfDuplicatesExistsinArguments(*args):
    args = sorted(args)

    if len(args) < 2:
        return False
    i = 0
    j = 1
    while (j < len(args)):
        if args[i] == args[j]:
            return True
        i = i + 1
        args[i] = args[j]
        j = j + 1

    return False


print(findIfDuplicatesExistsinArguments(1, 2, 3, 4, 5, 6, 7, 8))

# Explore this non linear approach aswell if you get time
# function areThereDuplicates() {
#   return new Set(arguments).size !== arguments.length;
# }
