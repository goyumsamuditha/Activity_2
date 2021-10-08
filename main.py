def recursive(a):
    if a == 1:
        return 1
    else:
        return a + recursive(a - 1)

from tot import tot
i = a
while i >= 0:
    print("Output:", recursive(i))
    i = int(input("Enter number:"))
print("Finished:")