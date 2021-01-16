class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        result = []
        appearances = {}
        for num in nums:
            if not num in appearances:
                appearances[num] = nums.count(num)

        for _ in range(k):
            result.append(self.key_with_max_value(appearances))

        return result

    def key_with_max_value(self, d: dict) -> int:
        max_value = 0
        max_key = 0
        for key, value in d.items():
            if value > max_value:
                max_value = value
                max_key = key
        d.pop(max_key)
        return max_key


def main():
    s = Solution()
    result = s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(result)


if __name__ == "__main__":
    main()
