class Solution:
    def groupThePeople(self, groupSizes: list) -> list:
        result = []
        cache_used_index = []
        for ii in range(len(groupSizes)):
            group = []
            for jj in range(len(groupSizes)):
                if (jj not in cache_used_index) and (groupSizes[ii] == groupSizes[jj]):
                    cache_used_index.append(jj)
                    group.append(jj)
                if len(group) == groupSizes[ii]:
                    break

            if len(group) == groupSizes[ii]:
                result.append(group)

        return list(sorted(result, key=lambda e: len(e)))


def main():
    s = Solution()
    result = s.groupThePeople([2,1,3,3,3,2])
    print(result)


if __name__ == "__main__":
    main()
