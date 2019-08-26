class Solution:
    def cat_word(self, secret, guess):
        secret_dict = {}
        guess_dict = {}
        A, B = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if secret[i] in secret_dict:
                    secret_dict[secret[i]] += 1
                else:
                    secret_dict[secret[i]] = 1

                if guess[i] in guess_dict:
                    guess_dict[guess[i]] += 1
                else:
                    guess_dict[guess[i]] = 1

        for j in secret_dict:
            if j in guess_dict:
                B += min(secret_dict[j], guess_dict[j])

        return str(A) + 'A' + str(B) + 'B'


if __name__ == '__main__':
    secret = '1014'
    guess = '4021'
    S = Solution()
    print(S.cat_word(secret, guess))
