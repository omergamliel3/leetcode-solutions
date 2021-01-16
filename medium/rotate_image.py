class Solution:
    def rotate(self, matrix: list) -> None:
        # martix length
        length = len(matrix)
        cache_matrix = []

        for ii in range(length):
            cache_matrix.append([])
            for jj in range(length):
                cache_matrix[ii].append(matrix[ii][jj])

        # modify the matrix by 90 degrees
        for ii in range(length):
            modify_index = length - ii
            for jj in range(length):
                matrix[jj][modify_index - 1] = cache_matrix[ii][jj]


def main():
    s = Solution()
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(f'Before: {matrix}')
    s.rotate(matrix)
    print(f'After: {matrix}')


if __name__ == "__main__":
    main()
