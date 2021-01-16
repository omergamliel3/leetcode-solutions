from itertools import combinations

class Solution:
    def numTeams(self, rating: list) -> int:
        teams = 0
        for comb in combinations(rating, 3):
            print(comb)
            i, j, k = comb
            if i > j > k or i < j < k:
                teams += 1
        return teams


def main():
    solution = Solution()
    result = solution.numTeams([1,2,3,4])
    print(result)


if __name__ == "__main__":
    main()
