def caesarCipherEncryptor(string, key):
    # My Solution, which sucks
    currSlice = string
    matched = False
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphIdx, shift = (0, 0)
    
    while shift < key:
        currSlice = alphabet[alphIdx: alphIdx + len(string)]

        if matched:
            shift += 1

        diff = len(string) - len(currSlice)
        if diff > 0:
            currSlice += alphabet[0: diff]
        
        if diff == len(string):
            # reset alphIdx to 1 and ctr = 0
            alphIdx = 0
            ctr = 0

        if currSlice == string:
            matched = True
        
        alphIdx += 1

    return currSlice

if __name__ == "__main__":
    print(caesarCipherEncryptor('xyzab', 3))
