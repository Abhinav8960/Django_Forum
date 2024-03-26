from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import Post
from .forms import PostForm 
# Create your views here.

def index(request):
    #if the method is post
    if request.method == 'POST':
        form=PostForm(request.POST)
       # if the form is valid 
        if form.is_valid():
             #yes , save
            form.save()
            # redirected to home
            return HttpResponseRedirect('/')

        else:
            #No , show error
            return HttpResponseRedirect(form.errors.as_json())



    #Get all the posts from db,limit=20
    posts = Post.objects.all()[:20]

    #show
    return render(request,'posts.html',{'posts':posts})


def delete(request,post_id):
    # Find user
    post = Post.objects.get(id= post_id)
    post.delete()
    return HttpResponseRedirect('/')
