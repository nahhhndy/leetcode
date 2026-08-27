class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(n):
            x = ord(target[i]) - ord('a')

            # Case 1: match target[i]
            if cnt[x] > 0:
                ans.append(target[i])
                cnt[x] -= 1
                continue

            # Cannot match target[i].
            # We need to increase an earlier position.
            break

        else:
            # Entire target matched.
            # target itself is NOT allowed.
            for j in range(n - 1, -1, -1):
                x = ord(target[j]) - ord('a')

                cnt[x] += 1
                ans.pop()

                # Find smallest character > target[j]
                for c in range(x + 1, 26):
                    if cnt[c]:
                        ans.append(chr(c + ord('a')))
                        cnt[c] -= 1

                        # Remaining characters in ascending order
                        for k in range(26):
                            ans.extend([chr(k + ord('a'))] * cnt[k])

                        return ''.join(ans)

            return ""

        # We failed to match target at position i.
        # Try increasing the current position first.
        for c in range(x + 1, 26):
            if cnt[c]:
                ans.append(chr(c + ord('a')))
                cnt[c] -= 1

                for k in range(26):
                    ans.extend([chr(k + ord('a'))] * cnt[k])

                return ''.join(ans)

        # Current position cannot be increased.
        # Backtrack and increase the latest matched position.
        for j in range(len(ans) - 1, -1, -1):
            x = ord(target[j]) - ord('a')

            # Put target[j] back into available characters.
            cnt[x] += 1
            ans.pop()

            # Smallest character > target[j]
            for c in range(x + 1, 26):
                if cnt[c]:
                    ans.append(chr(c + ord('a')))
                    cnt[c] -= 1

                    # Remaining suffix should be smallest possible.
                    for k in range(26):
                        ans.extend([chr(k + ord('a'))] * cnt[k])

                    return ''.join(ans)

        return ""