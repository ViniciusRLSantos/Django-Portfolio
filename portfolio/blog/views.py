from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
from .models import Posts
from .forms import CreatePostForm
from .serializers import PostsSerializer

# Create your views here.
class PostView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

def index(request):
    posts = Posts.objects.all()
    print(posts.count())
    if request.method == 'POST':
        data = request.POST
        post_id = data.get("delete")
        post = Posts.objects.get(id=post_id)
        post.delete()
        return HttpResponseRedirect('/home/')
    return render(request, 'blog/index.html', {'posts': posts})

def post_view(request, id):
    post = Posts.objects.get(id=id)
    return render(request, 'blog/post_view.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Post created!')
            return HttpResponseRedirect('/home/')
    else:
        form = CreatePostForm()    
    return render(request, 'blog/create_post.html', {'form': form})

def update_view(request, id):
    if request.method == 'POST':
        new_post = Posts.objects.get(id=id)
        print(new_post.title)
        form = CreatePostForm(request.POST, request.FILES, instance=new_post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Post Updated!')
            return HttpResponseRedirect('/home/')
    else:
        post = Posts.objects.get(id=id)
        form = CreatePostForm(instance=post)    
    return render(request, 'blog/update_post.html', {'form': form})
    