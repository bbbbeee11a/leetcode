class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        result = []

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in d:
                d[sorted_str].append(s)
            else:
                d[sorted_str] = [s]

        for key in d.keys():
            result.append(d[key])
        
        return result
        