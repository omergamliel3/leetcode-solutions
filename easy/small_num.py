class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i, value in enumerate(nums):
            smaller = 0
            for j, num in enumerate(nums):
                if i == j:
                    continue
                if value > num:
                    smaller += 1
            
            result.append(smaller)
            
        return result


def main():
    nums = [8,1,2,2,3]
    s = Solution()
    result = s.smallerNumbersThanCurrent(nums)
    print(result)

if __name__ == "__main__":
    main()
