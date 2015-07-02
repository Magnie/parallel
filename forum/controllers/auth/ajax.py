# AJAX for authentication
from django.contrib import auth
from django.utils import timezone
from django.http import JsonResponse
from forum.utils import valid_input, valid_request

def login(request):
    """
    desc: Validate login credentials
    params: str username, str password
    return: bool success
    """
    response = {
        'success': False
    }

    # Validate input
    if valid_request(request, need_auth=False):
            
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = auth.authenticate(username=username, password=password)
            
            # Login is successful
            if user is not None and user.is_active:
                auth.login(request, user)
                response['success'] = True

    # Return results
    return JsonResponse(response)

def register(request):
    """
    desc: Register a new user
    params: str username, str password, str passconf, str email
    return: bool success
    """
    pass

def logout(request):
    """
    desc: Logs out a user
    params: None
    return: bool success
    """
    pass
