def max_of_min(arr,k):
    n = len(arr)
    min_values = []
    for i in range(n-k+1):
        min_val = min(arr[i:i+k])
        min_values.append(min_val)
    return max(min_values)

k = int(input())
n = int(input())
arr = [int(input()) for i in range(n)]
result = max_of_min(arr,k)
print(result)