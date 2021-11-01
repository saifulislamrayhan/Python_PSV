n=int(input())
n=n-1
if n<20:
    def sa(n):
        if n>=0:
            sa(n-1)
            p = n * n
            print(p)

else:
    exit()
sa(n)


