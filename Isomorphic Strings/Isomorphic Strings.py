#User function Template for python3

class Solution:

    # Function to check if two strings are isomorphic.
    def areIsomorphic(self, s1, s2):

        char_mapping = defaultdict(chr)

        if (len(s1) != len(s2)):
            return False

        visited_chars = [0 for i in range(26)]

        for i in range(len(s1)):
            char1 = s1[i]
            char2 = s2[i]

            if (char1 not in char_mapping):
                if (visited_chars[ord(char2) - ord('a')]):
                    return False
                else:
                    visited_chars[ord(char2) - ord('a')] = 1
                    char_mapping[char1] = char2

            else:
                if (char_mapping[char1] != char2):
                    return False

        return True

