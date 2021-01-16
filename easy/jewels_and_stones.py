class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        for stone in stones:
            if stone in jewels:
                total += 1
                
        return total

def main():
    solution = Solution()
    result = solution.numJewelsInStones('aA', 'aAAbbbb')
    result = solution.numJewelsInStones('z', 'ZZ')
    print(result)


if __name__ == "__main__":
    main()
