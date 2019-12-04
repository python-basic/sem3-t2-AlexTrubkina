def main():
    repeat(1, 2, 1, 4, 2, 8)


def repeat(*n):
    arg = []
    for i in range(len(n)):
        j = i + 1
        while j < len(n):
            if n[i] == n[j]:
                arg.append(n[i])
            j += 1
    print(arg)


main()
