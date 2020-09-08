import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)
    ## textwrap.fill  wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)