def has_negatives(a):
    d = {}
    result = []
    for num in a:
        d[num] = 1
    for num in a:
        if (num*-1) in d and num > 0:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
