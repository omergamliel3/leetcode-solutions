
class Solution:
    def numTeams(self, rating: list) -> int:
        teams = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                for k in range(j + 1, len(rating)):
                    if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
                        teams += 1

        return teams


def main():
    solution = Solution()
    result = solution.numTeams([2,5,3,4,1])
    print(result)


if __name__ == "__main__":
    main()
