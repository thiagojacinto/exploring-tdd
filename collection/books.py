"""Books module to handle interactions to that resource"""

def search_books(author):
    """Search books by Author name"""
    data = prepare_request(author)
    url = get_url("https://go.to", data)
    execute(url)
    return author

def prepare_request(data):
    """Organize data to send request"""
    pass

def get_url(url, data):
    """Url to send the search request"""
    pass

def execute(url):
    """Execute http request"""
    pass