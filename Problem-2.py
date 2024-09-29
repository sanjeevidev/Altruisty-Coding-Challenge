def frog_count(s, start_index, end_index):
    n = len(s)
    left_stone = [-1] * n
    right_stone = [-1] * n
    nearest = -1
    for i in range(n):
        if s[i] == '|':
            nearest = i
        left_stone[i] = nearest
    nearest = -1
    for i in range(n-1, -1, -1):
        if s[i] == '|':
            nearest = i
        right_stone[i] = nearest
    cumulative_frogs = [0] * (n + 1)
    for i in range(1, n + 1):
        cumulative_frogs[i] = cumulative_frogs[i - 1] + (1 if s[i - 1] == '*' else 0)
    result = []
    for i in range(len(start_index)):
        start = start_index[i] - 1  
        end = end_index[i] - 1      
        right = right_stone[start]
        left = left_stone[end]
        if right == -1 or left == -1 or right >= left:
            result.append(0)
        else:
            result.append(cumulative_frogs[left + 1] - cumulative_frogs[right])  
    return result

s = input().strip()
n = int(input())
start_index = [int(input()) for _ in range(n)]
n = int(input())
end_index = [int(input()) for _ in range(n)]
result = frog_count(s, start_index, end_index)
for x in result:
    print(x)