class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_dict = Counter(words[0])
        for i in words:
            temp_dict = Counter(i)
            common_dict &= temp_dict
        return [key for key,value in common_dict.items() for _ in range(value)]
   
  