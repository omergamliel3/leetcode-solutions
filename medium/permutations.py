from itertools import permutations


class Solution:
    # first solution (recursion)
    def permute(self, nums: list) -> list:
        target_len = len(nums)
        res = []

        def inner(curr: list):
            if len(curr) == target_len:
                res.append(curr)
                return

            for num in nums:
                if not num in curr:
                    inner(curr + [num])

        inner([])
        return res

    # second solution (itertools permutations)
    def another_permute(self, nums: list) -> list:
        res = []
        for perm in permutations(nums, len(nums)):
            res.append(list(perm))
        return res


def main():
    s = Solution()
    res = s.permute([1, 2, 3, 4])
    print(res)


if __name__ == "__main__":
    main()
