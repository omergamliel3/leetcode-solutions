class Solution:
    def subsets(self, nums: list) -> list:
        output = [[]]

        for num in nums:
            print(f'current num: {num}')
            print(output)
            output += [curr + [num] for curr in output]
            print(output)

        return output


def main():
    s = Solution()
    result = s.subsets([4, 1, 0])
    print(result)


if __name__ == "__main__":
    main()
