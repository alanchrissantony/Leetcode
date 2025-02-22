class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        dt={'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        left = right = vowel = count = 0
        for i in range(len(word)):
            if word[i] in dt:
                dt[word[i]]+=1

                if dt[word[i]] == 1:
                    vowel+=1
                while vowel == 5:
                    dt[word[right]] -= 1
                    if dt[word[right]] == 0:
                        vowel -= 1
                    right+=1
                count+=right-left
            else:
                dt={'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
                left = right = i+1
                vowel = 0

        return count


            
