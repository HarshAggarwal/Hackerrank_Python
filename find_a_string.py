def count_substring(string, sub_string):
    for i in range(len(string)):
        if string == sub_string:
            counter = counter+1
        else:
            pass
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)