A = "GUGPUAGAFQBMPYAGGAAOALAELGGGAOGLGEGZ"
count = 0
times = 0
pointer = -1
for i in A:
    if i == 'G':
        count += 1
for i in A:
    if i == 'A' and pointer == -1:
        times += count
    elif i == 'G':
        count -= 1
        pointer = 0
    elif i == 'A' and pointer == 0:
        times += count

print(times)

