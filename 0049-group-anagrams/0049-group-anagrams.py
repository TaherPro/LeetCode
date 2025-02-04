class Solution:
    def groupAnagrams(slef, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # created a list of zeros for each letter

            for c in s:
                count [ord(c) - ord("a")] += 1 # count the letter frequncy 
            
            res[tuple(count)].append(s) # convert list to tuple and store in dict

        return list(res.values())

