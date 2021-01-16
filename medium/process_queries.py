class Solution:
    def processQueries(self, queries: list, m: int) -> list:
        res = []
        p = [x for x in range(1, m+1)]
        print(f'p list: {p}')
        for query in queries:
            pos = p.index(query)
            print(f'position of {query} in P is {pos}')
            res.append(pos)
            p.insert(0, p.pop(pos))
        return res


def main():
    s = Solution()
    res = s.processQueries([3, 1, 2, 1], 5)
    print(res)


if __name__ == "__main__":
    main()
