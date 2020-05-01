from utils import *
from URL import *

# some keywords
keywords = ['basketball', 'england', 'soccer', 'ferrari', 'olympics', 'messi']

for keyword in keywords:
    # to store the frequency of a pattern with the corresponding url we are going to create a list of dictionaries
    # containing the webpage url and its frequency
    url_dict = []
    print(f"Searching word: {keyword}")
    print('-' * 70)
    for url in all_url:
        # get web page data from the url
        text = getWebpage(url)
        # search the pattern in the data extracted and get the frequency
        keyword_freq = (search(text.lower(), keyword.lower()))
        sport = (search(text.lower(), 'sport'))
        print(f"{url} processed")
        # store the url and frequency into the list if the keyword is found in the web page
        if keyword_freq > 1:
            # to recommend the best webpage related to sports and the keyword we are going to find a ratio between this
            # two, that is: sport_freq / keyword_freq
            # The closest the ratio is to 1, the better
            ratio = sport / keyword_freq
            url_dict.append(dict({'url': url, 'keyword_frequency': keyword_freq, 'sport': sport, 'ratio': ratio}))

    print()
    print("-" * 70)
    print("Searching finished")

    # get the web page which has the ratio closest to 1
    recommended_webpage = min(url_dict, key=lambda x: abs(x['ratio'] - 1))
    print(f"Recommended webpage {recommended_webpage['url']}")
    print("-" * 70)