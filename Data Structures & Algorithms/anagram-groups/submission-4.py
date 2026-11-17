class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            freq_map = [0]*26
            for ch in s:
                i = ord(ch) - ord('a')
                freq_map[i] += 1
            k = tuple(freq_map) #keys cant be iterable
            anagram[k].append(s)
        return list(anagram.values())
