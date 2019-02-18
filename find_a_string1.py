a = input()
suba = input()
cnt = 0
for i in range(len(a)):
    if(a[i:].startswith(suba)):
        cnt+=1
    else:
        continue
print(cnt)


'''string = raw_input()
substring = raw_input()

count = 0
for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)] == substring:
        count += 1
print count'''
