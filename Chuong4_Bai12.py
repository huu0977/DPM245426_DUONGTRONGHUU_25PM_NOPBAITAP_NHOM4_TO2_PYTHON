print("Hàm oscillate")


def oscillate(start, end):
    for n in range(start, end):
        yield n
        yield -n


for n in oscillate(-3,5):
    print(n,end='')
print()
