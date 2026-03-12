scores=[45,55,30,70,25,60]
passed=0
for score in scores:
    if score>=40:
        passed+=1
print(f"Passed: {passed}")

# pairs summing 100
for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        if scores[i] + scores[j] == 100:
            print(f"Pair: ({scores[i]}, {scores[j]})",end=" ")