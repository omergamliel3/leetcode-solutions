# solution with the help of permutations from itertools module

from itertools import permutations


class Solution:
    def numTeams(self, rating: list) -> int:
        result = 0
        perms = list()
        for item in permutations(rating, 3):
            if self.validatePermIndex(item, rating):
                perms.append(list(item))

        for perm in perms:
            if self.validatePermAscending(perm) or self.validatePermDescending(perm):
                result += 1
        return result

    def validatePermIndex(self, perm: list, rating: list) -> bool:
        valid = True
        for i in range(0, len(perm) - 1):
            if rating.index(perm[i]) > rating.index(perm[i + 1]):
                valid = False
                break
        return valid

    def validatePermAscending(self, perm: list) -> bool:
        valid = True
        for i in range(0, 2):
            if not perm[i] < perm[i + 1]:
                valid = False
                break
        return valid

    def validatePermDescending(self, perm: list) -> bool:
        valid = True
        for i in range(0, 2):
            if not perm[i] > perm[i + 1]:
                valid = False
                break
        return valid


def main():
    print([0] * 10)
    solution = Solution()
    result = solution.numTeams([2, 1, 3])
    print(f'result: {result}')


if __name__ == "__main__":
    main()
