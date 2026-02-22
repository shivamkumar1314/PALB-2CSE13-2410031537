arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

if len(arr) <= 1:
    print(0)

max_reach = arr[0]
step = arr[0]
jump = 1

for i in range(1, len(arr)):
    if i == len(arr) - 1:
        print(jump)
        break

    max_reach = max(max_reach, i + arr[i])
    step -= 1

    if step == 0:
        jump += 1
        if i >= max_reach:
            print(-1)
            break
        step = max_reach - i