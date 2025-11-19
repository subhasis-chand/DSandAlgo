def recPermutations(src, s, result):
    if src == len(s):
        result.append(''.join(s))
        return
    
    for i in range(src, len(s)):
        print('src:', src, 'i:', i)
        s[src], s[i] = s[i], s[src]
        recPermutations(src + 1, s, result)
        s[src], s[i] = s[i], s[src]  # backtrack

def findAllPermutations(s):
    result = []
    recPermutations(0, list(s), result)
    return result

if __name__ == "__main__":
    s = "ABC"
    permutations = findAllPermutations(s)
    print("All Permutations of the string are:")
    for perm in permutations:
        print(perm)

