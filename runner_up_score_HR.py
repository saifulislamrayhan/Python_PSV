A = []
B=[]
n = int(input())
if (n >= 2) & (n<=10):
    for i in range(0, n):
        ele = int(input())
        if (ele>=-100) & (ele<=100):
            A.append(ele)
            for i in A:
                if i not in B:
                    B.append(i)
        else:
            exit()
else:
    exit()
B.sort(reverse=True)
print(B[1])
