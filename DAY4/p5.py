scores = [3, 8, 2, 7, 5, 9, 1, 6]
print(f"Highest signal: {max(scores)}")
for i in range(7):
    check = scores[i] + scores[i + 1]
    if check > max(scores):
        maxi=check
print(f"Highest pair signal: {maxi}")

print("raising triplets:")
for i in range(6):
    check = scores[i] + scores[i + 1] + scores[i + 2]
    if check > max(scores):
        maxi=check
print(f"Highest triplet signal: {maxi}")