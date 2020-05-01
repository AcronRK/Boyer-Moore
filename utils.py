import requests
from bs4 import BeautifulSoup

NO_OF_CHARS = 256

def badCharHeuristic(string, size):
    # Initialize all occurrence as -1
    badChar = [-1] * NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i

        # return initialized list
    return badChar


def search(txt, pat):
    # cnt will be used to measure the frequency of a pattern in the text
    cnt = 0
    m = len(pat)
    n = len(txt)

    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m)

    # s is shift of the pattern with respect to text
    s = 0
    while s <= n - m:
        j = m - 1

        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j < 0:
            # increment frequency(how many times the pattern occurred)
            cnt += 1
            '''     
                Shift the pattern so that the next character in text 
                      aligns with the last occurrence of it in pattern. 
                The condition s+m < n is necessary for the case when 
                   pattern occurs at the end of text 
               '''
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            ''' 
               Shift the pattern so that the bad character in text 
               aligns with the last occurrence of it in pattern. The 
               max function is used to make sure that we get a positive 
               shift. We may get a negative shift if the last occurrence 
               of bad character in pattern is on the right side of the 
               current character. 
            '''
            s += max(1, j - badChar[ord(txt[s + j])])
    return cnt


def getWebpage(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding="latin-1")
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    # get text
    text = soup.get_text()
    text = text.encode('utf-8').decode('latin-1')
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text
