# 小红拿到了一个数组，她每次操作可以选择两个元素，将它们变成它们的平均数（当且仅当这两个元素的平均数为整数时才可操作）。小红想知道，自己能否通过一次操作，使得所有元素的乘积为偶数？
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    mod4_1=0
    mod4_3=0
    for i in arr:
        if i%2==0:
            print("YES")
            break
        elif i%4==1:
            mod4_1+=1
            if mod4_3>0:
                print("YES")
                break
        elif i%4==3:
            mod4_3+=1
            if mod4_1>0:
                print("YES")
                break
    print("NO")
            
            
            