from googlesearch import search


# Define a function to search for terms on a specific domain using Google Search.
def search_term(topic, count=5):
    search_terms = ["exploit wild", "vulnerability mitigation", "security blog", "patch detection", "new zeroday",
                    "securing", "critical alert"]
    # Create an empty list to store the resulting URLs.
    urls = []
    # Iterate through each search term provided in the search_terms list.
    for term in search_terms:
        # Use the Google Search library to perform a search combining the domain and search term.
        # num_results specifies the number of search results to retrieve for each term.
        for url in search(f"{topic} {term}", num_results=count):
            # Append the retrieved URL to the urls list.
            urls.append(url)

    # Remove duplicates by converting the list to a set and then sorting it.
    return sorted(set(urls))
