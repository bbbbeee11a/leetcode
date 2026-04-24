# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d = {}
#         result = []

#         for s in strs:
#             sorted_str = ''.join(sorted(s))
#             if sorted_str in d:
#                 d[sorted_str].append(s)
#             else:
#                 d[sorted_str] = [s]

#         for key in d.keys():
#             result.append(d[key])
        
#         return result
        
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            d[key].append(s)

        return list(d.values())