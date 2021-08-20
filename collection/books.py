from urllib.request import urlopen

"""Books module to handle interactions to that resource"""

def search_books(author):
    """Search books by Author name"""
    data = prepare_request(author)
    url = get_url("https://go.to", data)
    return execute(url)

def prepare_request(data):
    """Organize data to send request"""
    pass

def get_url(url, data):
    """Url to send the search request"""
    pass

def execute(url):
    """Execute http request"""
    pass

def execute_url(url):
    """Execute http request by calling urlopen"""
    with urlopen(url, timeout = 13) as response:
        result = response.read().decode("utf-8")
    return result