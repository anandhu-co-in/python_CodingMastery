PI = "314159265358979323846263383279"
IN = ['314', '49', '9001', '15926535897', '14', '9323', '846263383279', '4', '793']


def pos(p):
    minspaces = -2
    if p == len(PI)+1:
        return 0
    for i in range(p + 1, len(PI) + 1):
        print(i)
        if PI[0:i] in IN:
            if pos(i + 1) != -2:
                if minspaces == -2 : minspaces=1
                minspaces = min(minspaces, 1 + pos(i + 1))
    return minspaces


pos(0)
print(pos(0))

123

1, 23


#Damn this proble is gonna break my brain.
#Giving up for today!