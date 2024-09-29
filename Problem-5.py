def training(oxygen):
    num_trainee = 3
    num_round = 3
    if len(oxygen) != num_trainee * num_round:
        return "INVALID INPUT"
    for i in oxygen:
        if i < 1 or i > 100:
            return "INVALID INPUT"
    average = []
    for i in range(num_trainee):
        avg = sum(oxygen[i::num_trainee]) / num_round
        average.append(round(avg))
    max_average = max(average)
    if max_average < 70:
        return "All trainees are unfit"
    fit_trainee = []
    for i in range(num_trainee):
        if average[i] == max_average:
            fit_trainee.append(f"Trainee Number : {i+1}")
    return "\n".join(fit_trainee)

oxygen = []
for i in range(9):
    oxygen.append(int(input().strip()))
result = training(oxygen)
print(result)