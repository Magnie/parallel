from django.shortcuts import render

# Create your views here.

def index(request):
    "Redirects to the home tag or can be used as a landing page."
    response = {
        'view': 'forum/index.html',
    }
    return render(request, 'forum/container.html', response)
