import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text = string)
    for i in word_list:
        print(i)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    #print(result)

#or
'''import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
	print(result)'''
