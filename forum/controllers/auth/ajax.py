# AJAX for authentication
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth.models import User
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
        'success': False,
        'username': '',
    }

    # Validate input
    if valid_request(request, need_auth=False):
        username = request.POST['username'].lower()
        password = request.POST['password']
        if username and password:
            user = auth.authenticate(username=username, password=password)
            
            # Login is successful
            if user is not None and user.is_active:
                auth.login(request, user)
                response['username'] = user.username
                response['success'] = True

    # Return results
    return JsonResponse(response)

def register(request):
    """
    desc: Register a new user
    params: str username, str password, str passconf, str email
    return: bool success
    """
    response = {
        'success': False,
        'username': '',
    }

    # Validate input
    if valid_request(request, need_auth=False):
            
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email'].lower()
        username = request.POST['username'].lower()
        password = request.POST['password']
        if first_name and last_name and email and username and password:
            users = User.objects.filter(
                Q(username=username) | (
                    Q(first_name=first_name) &
                    Q(last_name=last_name)
                )
            ).count()
            if users == 0:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                auth.authenticate(username=username, password=password)
                response['username'] = user.username
                response['success'] = True
                
    
    # Return results
    return JsonResponse(response)

def logout_ajax(request):
    """
    desc: Logs out a user
    params: None
    return: bool success
    """
    response = {
        'success': False,
        'username': '',
    }
    auth.logout(request)
    
    response['success'] = True
    
    # Return results
    return JsonResponse(response)
