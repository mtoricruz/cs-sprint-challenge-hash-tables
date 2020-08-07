def intersection(arrays):
    d = {}
    result = []
    for arr in arrays:
        for each_num in arr:
            if each_num in d:
                d[each_num] += 1
            else:
                d[each_num] = 1
    
    for i in d:
        if d[i] > 1:
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
