class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Prepend the length of the string and a delimiter like '#'
            res += str(len(s)) + "#" + s
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0  # Pointer to track our position in the string
    
        while i < len(s):
            j = i
            # Find the position of the '#' delimiter
            while s[j] != '#':
                j += 1
            
            # Extract the length of the upcoming word
            length = int(s[i:j])
        
            # Extract the actual word using the length
            # (j + 1 skips past the '#')
            word = s[j + 1 : j + 1 + length]
            res.append(word)
        
            # Move the pointer to the start of the next encoded word
            i = j + 1 + length
        
        return res 
