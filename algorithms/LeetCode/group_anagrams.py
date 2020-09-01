class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in groups:
                groups[key] += [word]
            else:
                groups[key] = [word]
        for key in groups:
            anagrams.append(groups[key])
        return anagrams


if __name__ == "__main__":
    print(Solution.groupAnagrams(["dggggg", "ddddddg"]))