t = [False, True]

print("~(A V ~B)")
for A in t:
    for B in t:
        print(A or not B)

print("~A V B")

for A in t:
    for B in t:
        print((not A or B) and not (A and not B))

for A in t:
    for B in t:
        for C in t:
            print(not(A or B) or ((A or C) and not(B or not C)))
