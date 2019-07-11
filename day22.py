#2019.7.11 lixs
#字母异位词分组

"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""
class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return []
        lib = {}
        res = []
        for st in strs:
            tmp = "".join(sorted(st))
            if tmp not in lib:
                lib[tmp] = [st]
            else:
                lib[tmp] = lib[tmp] + [st]
        print(lib)
        for val in lib:
            res.append(lib[val])
        return res


if __name__ == "__main__":
    train = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = train.groupAnagrams(strs)
    print(res)
