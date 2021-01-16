class Solution:
    def generateParenthesis(self, n: int) -> list:

        res = []

        def inner(curr, l, r):

            # if current string hit n*2
            # thats when you back out!
            if len(curr) == n*2:
                res.append(curr)
                return

            # keep adding left parens until no more remaining
            if l > 0:
                inner(curr+"(", l-1, r)

            # keep adding right parens if a left matches it
            # and there are remaining
            if r > 0 and l < r:
                inner(curr+")", l, r-1)

        inner("", n, n)
        return res
