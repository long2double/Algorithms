class Solution:
    def temple(self, refer, target):
        if len(refer) != len(target):
            return False

        hash = {}
        used = {}
        for i in range(len(refer)):
            if refer[i] not in hash:
                if target[i] in used:
                    return False
                hash[refer[i]] = target[i]
                used[target[i]] = True
            else:
                if hash[refer[i]] != target[i]:
                    return False
        return True


if __name__ == '__main__':
    refer = ['1', '2', '2', '3', '1', '2', '3']
    target = ['A', 'B', 'B', 'C', 'A', 'B', 'C']
    S = Solution()
    print(S.temple(refer, target))