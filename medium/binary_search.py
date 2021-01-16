from math import floor


def binary_search(array: list, n: int) -> int:
    res = []

    def inner(curr):
        mid = floor(len(curr) / 2)
        key = curr[mid]
        if key == n:
            res.append(array.index(key))
            return
        if key > n:
            inner(curr[:mid])
        else:
            inner(curr[mid+1:])

    inner(array)
    return res[0]


def simple_search(array: list, num: int) -> int:
    for i in range(len(array)):
        if array[i] == num:
            return i


def main():
    res = binary_search([0, 1, 2, 3, 4, 5], 5)
    print(res)


if __name__ == "__main__":
    main()
