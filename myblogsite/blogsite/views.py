from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

# Create your views here.
#all posts
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blogsite/post/listss.html', {'posts':posts})

#single post
def post_details(request, year, month, day, post):
    post = get_object_or_404(Post, status =Post.Status.PUBLISHED,
                             slug =post,
                             publish_year=year,
                             publish_month=month,
                             publish_day = day)
    return render(request, 'blogsite/post/details.html', {'post':post} )

  

