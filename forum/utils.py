import itertools

# Settings
TOPICS_PER_PAGE = 20
POSTS_PER_PAGE = 5

def valid_input(data, _type):
    "Return the input if it matches the _type"
    try:
        data = _type(data)
    
    except:
        pass
    
    return data if type(data) == _type else False

def valid_request(request, need_auth=True, method='POST'):
    """
    Check if user is authenticated, there is POST data, and the test cookie
    worked.
    """
    if request.user.is_authenticated() == need_auth and \
            request.method == method:
        return True
        
    return False

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)
