# AJAX for navigation
from django.utils import timezone
from django.http import JsonResponse
from forum.models import Tag, Topic, Post
from forum.utils import valid_input, valid_request
from django.core.urlresolvers import reverse

def get_nav(request):
    """
    desc: Get a list navigation menus
    params: void
    return: array({str name, str url}) items
    """
    response = {
        'success': False,
        'items': [],
        'data': {
            # Index number of the items to indicate the login button.
            'login': -1,
            'logout': -1,
        },
    }
    items = []
    data = {}
    
    if valid_request(request, method='GET'):
        name = '{0} {1}'.format(request.user.first_name, request.user.last_name)
        if name == ' ':
            name = request.user.username
            
        items.append({'name': 'Index', 'url': reverse('index')})
        items.append({'name': 'Home', 'url': reverse('tag', args=[1])})
        items.append({'name': 'Logout', 'url': ''})
        items.append({'name': name, 'url': ''})
        data['logout'] = 'Logout'
        
        response['success'] = True
    
    else:
        items.append({'name': 'Home', 'url': reverse('index')})
        items.append({'name': 'Login', 'url': ''})
        data['login'] = 'Login'
        
        response['success'] = True
    
    response['items'] = items
    response['data'] = data
    
    # Return results
    return JsonResponse(response)

def get_breadcrumbs(request, page, pid):
    """
    desc: Get the parenting tags of a topic or another tag
    params: str page, int pid
    return array({str tag_name, id tag_id})
    """
    response = {
        'success': False,
        'tags': [],
    }
    if page and pid:
        if page == 'topic':
            topic = Topic.objects.get(pk=pid)
            temp_tags = Tag.objects.filter(topics=topic)
        elif page == 'tag':
            tag = Tag.objects.get(pk=pid)
            temp_tags = Tag.objects.filter(tags=tag)
        
        tags = []
        for t in temp_tags:
            tags.append({
                'tag_name': t.name,
                'tag_id': t.id,
            })
        
        response['tags'] = tags
        
        response['success'] = True
    
    # Return results
    return JsonResponse(response)

def get_subtags(request, tag_id):
    """
    desc: Get the parenting tags of a topic or another tag
    params: str page, int pid
    return array({str tag_name, id tag_id})
    """
    response = {
        'success': False,
        'tags': [],
    }
    if tag_id:
        tag = Tag.objects.get(pk=tag_id)
        temp_tags = tag.tags.all()
        
        tags = []
        for t in temp_tags:
            tags.append({
                'tag_name': t.name,
                'tag_id': t.id,
            })
        
        response['tags'] = tags
        
        response['success'] = True
    
    # Return results
    return JsonResponse(response)
