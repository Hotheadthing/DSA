flowerbed = [1,0,0,0,1]
n = 1
flowerbed = [1,0,0,0,1]
n = 2
counter = 0
for i in range(len(flowerbed)):
    if flowerbed[i] == 0:
        if (i+1 < len(flowerbed)-1) and (i+2 <= len(flowerbed)-1):
            if flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                counter += 1
    if (flowerbed[i] == 0) and i == 0:
        if i+1 < len(flowerbed)-1:
            if flowerbed[i+1] == 0:
                counter += 1
    if (i == len(flowerbed)-1) and (flowerbed[i] == 0):
        if flowerbed[i-1] == 0:
            counter += 1

if counter >= n:
    print(True)
else:
    print(False)