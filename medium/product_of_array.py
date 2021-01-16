class Solution:
    def productExceptSelf(self, nums: list) -> list:
        res = []
        for ii in range(len(nums)):
            curr = 1
            for jj in range(len(nums)):
                if not ii == jj:
                    curr *= nums[jj]

            res.append(curr)

        return res

    def productExceptSelfAnother(self, nums: list) -> list:
        res = []
        total = 1
        for num in nums:
            total *= num
        for i in range(len(nums)):
            res.append(total // nums[i])

        return res


def main():
    s = Solution()
    result = s.productExceptSelfAnother([1, 2, 3, 4])
    print(result)


if __name__ == "__main__":
    main()
