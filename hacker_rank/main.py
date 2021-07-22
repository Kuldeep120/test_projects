import questions as qs
if __name__ == '__main__':
    # with open('input.txt','r') as fp:
    #     while True:
    #         data = fp.readline()
    #         if data:
    #             print(hackerrankInString(data))
    print(qs.pangram.pangrams('We promptly judged antique ivory buckles for the prize'))
    print(qs.pangram.pangrams('We promptly judged antique ivory buckles for the next prize'))