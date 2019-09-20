class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern = list(pattern)
        str = str.split(' ')
        p_has = {}
        s_has = {}
        for p, s in zip(pattern, str):
            print(p_has)
            if p not in p_has:
                p_has[p] = s
            else:
                if p_has[p] != s:
                    return False

        return True


if __name__ == '__main__':
    S = Solution()
    p = "abba"
    s = "dog cat cat dog"
    print(S.wordPattern(p, s))
