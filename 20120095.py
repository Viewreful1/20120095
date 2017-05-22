def dfs(x):
    visited[x]=1
    print(x, end=' ')
    for y in adj[x]:
        if visited[y]==0:
            dfs(y)

def bfs(x):
    print(x, end=' ')
    visited[x]=1
    queue.append(x)
    while (queue!=[]):
        x=queue.pop(0)
        for y in adj[x]:
            if visited[y]==0:
                print(y, end=' ')
                queue.append(y)
                visited[y]=1

s=input().split()
vnum=int(s[0])
enum=int(s[1])
start=int(s[2])
adj=[[] for i in range(vnum+1)]
visited=[0 for i in range(vnum+1)]
queue=[]
for i in range(enum):
    s=input().split()
    adj[int(s[0])].append(int(s[1]))
    adj[int(s[1])].append(int(s[0]))
for i in range(1, vnum+1):
    adj[i].sort()
dfs(start)
visited=[0 for i in range(vnum+1)]
print()
bfs(start)