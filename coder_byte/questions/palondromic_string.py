def palindromic_substring(str_param):
    long_palendrom = ""
    for i in range(len(str_param)):
        for j in range(len(str_param), i, -1):
            sub = str_param[i:j]
            if sub == sub[::-1]:
                if len(long_palendrom) <= len(sub):
                    long_palendrom = sub

    return None if len(long_palendrom) <= 1 else long_palendrom


def run():
    print(palindromic_substring('hellosannasolleh'))
