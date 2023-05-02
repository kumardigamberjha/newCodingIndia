from django.shortcuts import render, redirect
from blogs.forms import *
from blogs.models import AddBlog, Playlist, SomeModel

# Create your views here.
def index(request):
    blogs = AddBlog.objects.all()
    play = Playlist.objects.all()
    ran = AddBlog.objects.order_by('?')
    # tags = AddBlog.tags.all()
    context = {'blogs':blogs, 'ran': ran, 'play':play}
    # Random element 4
    return render(request, "blogs/index.html", context)

def addblog(request):
    form = AddBlogForm()
    somemodel = SomeModel.objects.all()
    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES)

        title = request.POST['title']
        if AddBlog.objects.filter(title=title).exists():
            raise Exception("Blog Title Already Exists")

        if form.is_valid():
            form.save()
            return redirect("blogs_index")
    
    context = {'form':form, 'somemodel': somemodel}
    return render(request, 'blogs/addblog.html', context)

def Readblog(request, post_id):
    blogs = AddBlog.objects.get(pk = post_id)
    read = {'blogs':blogs}
    return render(request, 'blogs/readblogs.html', read)

def TagsBlog(request, id=id):
    tag = AddBlog.tags.get(id=id)
    return render(request, 'blogs/tagsblog.html', {'tags': tag})

def ReadPlay(request, post_id):
    plays = Playlist.objects.get(pk = post_id)
    blogs = AddBlog.objects.filter(play=plays)
    read = {'blogs':blogs, 'play':plays}
    return render(request, "blogs/read_play.html", read)


