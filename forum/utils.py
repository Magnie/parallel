import itertools

def valid_input(data, _type):
    "Return the input if it matches the _type"
    try:
        data = _type(data)
    
    except:
        pass
    
    return data if type(data) == _type else False

def valid_request(request, need_auth=True):
    """
    Check if user is authenticated, there is POST data, and the test cookie
    worked.
    """
    if request.user.is_authenticated() == need_auth and \
            request.method == 'POST' and \
            request.session.test_cookie_worked():
        return True
        
    return False

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)
