class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Can be done with default dict,ord and tuple but going with bit more complex
        #sorting gives all the anagrams side by side
        hashmap = {}
        for word in strs:
            sortedletter = sorted(word) #Each aplhabet is seperated
            sortedword = ''.join(sortedletter) #Joining all letters to get sortedword
            if sortedword not in hashmap:
                hashmap[sortedword] = [word]
            else:
                hashmap[sortedword].append(word)
        return hashmap.values()
