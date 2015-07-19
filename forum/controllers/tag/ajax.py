# AJAX for tags

"""
Model Reference
-----
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    tags = models.ManyToManyField("self", blank=True, symmetrical=False)
    itopics = models.ManyToManyField("Topic", blank=True)
    
    groups = models.ManyToManyField("FGroup", blank=True)
    permissions = models.ManyToManyField("FPermission", blank=True)


AJAX Function Template
-----
response = {
    'success': False
}

# Validate input

# Execute

# Return results
return JsonResponse(response)
-----


"""

from django.utils import timezone
from django.http import JsonResponse
from forum.models import Tag, Topic, Post, TagTopic
from forum.utils import valid_input, valid_request

def get_tags(request, tag_id):
    """
    desc: Get sub-tags of a tag
    params: int tag_id
    return: bool success, array({str tag_name, int tag_id}) tags
    """
    response = {
        'success': False,
        'tags': []
    }
    
    # Validate input
    if tag_id:
        tag = Tag.objects.get(pk=tag_id)
        if tag:
            
            # Get the tags
            sub_tags = []
            for t in tag.tags:
                sub_tags.append({
                    'id': t.id,
                    'name': t.name
                })
            
            # Set the response
            response['tags'] = sub_tags
            
            # Everything was successful!
            response['success'] = True
    
    # Return results
    return JsonResponse(response)

def create_tag(request):
    """
    desc: Create a new tag
    params: str tag_name, array(int tag_id) sub_tags,
    return: bool success, str tag_name, id tag_id
    """
    response = {
        'success': False,
        'tag_name': '',
        'tag_id': -1
    }
    
    # Validate input
    if valid_request(request):
        tag_name = request.POST['tag_name']
        parent_id = request.POST['parent_id']
        post_date = timezone.now()
        
        if tag_name and parent_id:
            # Create new tag and update parent tag with new tag.
            parent_tag = Tag.objects.filter(id=parent_id)
            new_tag = Tag(
                name=tag_name
            )
            new_tag.save()
            
            parent_tag.tags.add(new_tag)
            parent_tag.save()
            
            # Set response
            response['tag_name'] = new_tag.name
            response['tag_id'] = new_tag.id
            
            # Everything was successful!
            response['success'] = True
    
    # Return results
    return JsonResponse(response)

def modify_tag(request):
    """
    desc: Modify a tag's name, sub-tags,
    params: int tag_id, str action (add/remove/new_name), value (sub_tag_id, name)
    return: bool success
    """
    pass

def delete_tag(request):
    """
    desc: Delete a tag
    params: int tag_id
    return: bool success
    """
    pass

def search_tag(request):
    """
    desc: Return search results for a specific tag
    params: str tag_name
    return: array([str tag_name, int tag_id]) tags
    """
    pass

def itopic(request):
    """
    desc: Modify a tag's important topics.
    params: int tag_id, str action (add/remove), int topic_id
    return: bool success
    """
    pass
