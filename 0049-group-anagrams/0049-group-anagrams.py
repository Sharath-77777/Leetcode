class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for i in strs:
            counts = [0]*26
            for j in i:
                k = ord(j) - ord("a")
                counts[k]+=1
            res[tuple(counts)].append(i)
        return res.values()