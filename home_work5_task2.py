def binary_search(arr, x, accuracy=2):
    print("Release:", arr)
    low = 0
    high = len(arr) - 1
    mid = 0
    counter = 0
    max_step = 0
    round_x = round(x, accuracy)
    while low <= high:
        mid = int((high + low) // 2)
        max_step = max(max_step, mid)
        counter += 1
        cur_value = round(arr[mid], accuracy)
        print("mid=", mid, "cur_value=", cur_value)
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if cur_value < round_x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif cur_value > round_x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (counter, arr[max_step+1])

    # якщо елемент не знайдений
    return (counter, f"{arr[max_step]}")


arr = [2/19, 3/8, 4/7, 10/15, 40/45]
x = 0.57

result = binary_search(arr, x, 2)
print(f"Step: {result[0]}, directed to {result[1]}")
