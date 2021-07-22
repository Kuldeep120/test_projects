def hackerrankInString(s):
    hack = "hackerrank"
    index = 0
    for i in range(len(s)):
        if hack[index] == s[i]:
            index += 1
        if index == 10:
            return "YES"
    return "NO"