def odd_balloon(n,balloons):
    balloon_count = {}
    for i in balloons:
        if i in balloon_count:
            balloon_count[i]+=1
        else:
            balloon_count[i]=1
    for j in balloons:
        if balloon_count[j]%2!=0:
            return j
    return 'All are even'

n = int(input())
balloons = [input().strip() for i in range(n)]
result = odd_balloon(n,balloons)
print(result)