class Solution(object):
    def groupAnagrams(self, strs):
        word_map = {}
        for word in strs:
            sstring = ''.join(sorted(word))
            if sstring not in word_map:
                word_map[sstring] = [word]
            else:
                word_map[sstring].append(word)
        return(list(word_map.values()))