from collections import defaultdict
d = defaultdict(list)
n,m = map(int,input().split())
for i in range(n):
    vt = input()
    d[vt].append(i+1)
for j in range(m):
    vt = input()
    if vt in d:
        print(*d[vt])
    else:
        print(-1)
