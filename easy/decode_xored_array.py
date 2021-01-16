class Solution:
    def decode(self, encoded: list, first: int) -> list:
        result = [first]
        for num in encoded:
             result.append(num^result[-1])
        return result


def main():
    s = Solution()
    result = s.decode([1,2,3], 1)
    print(result)



if __name__ == "__main__":
    main()
