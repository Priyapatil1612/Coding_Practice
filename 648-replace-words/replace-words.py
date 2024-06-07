class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sent_li = sentence.split()
        j = 0
        while j < len(dictionary):
            for i in range(len(sent_li)):
                if sent_li[i].startswith(dictionary[j]):
                    sent_li[i] = dictionary[j]
            j = j + 1
        return " ".join(sent_li)