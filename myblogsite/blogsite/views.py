from django.shortcuts import render
from .models import Post
from django.http import Http404

# Create your views here.
#all posts
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blogsite/post/listss.html', {'posts':posts})

#single post
def post_details(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post Found")
    return render(request, 'blogsite/post/details.html', {'post':post})

