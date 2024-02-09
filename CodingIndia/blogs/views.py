from django.shortcuts import render, redirect
from blogs.forms import *
from django.core.paginator import Paginator
from blogs.models import AddBlog, Playlist

######################## Views ##################################
def index(request):
    blogs = AddBlog.objects.all().order_by('-pub_date')
    play = Playlist.objects.all()
    paginator = Paginator(blogs, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ran = AddBlog.objects.order_by('?')[0]

    context = {'page_obj':page_obj, 'ran': ran, 'play':play}
    return render(request, "blogs/index.html", context)


def addblog(request):
    form = AddBlogForm()
    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES)

        title = request.POST['title']
        if AddBlog.objects.filter(title=title).exists():
            raise Exception("Blog Title Already Exists")

        if form.is_valid():
            form.save()
            return redirect("blogs_index")
    
    context = {'form':form}
    return render(request, 'blogs/addblog.html', context)


def Readblog(request, slug):
    blogs = AddBlog.objects.get(slug = slug)
    randomBlogs = AddBlog.objects.exclude(slug=slug).order_by('pub_date')[:3]
    playlist = Playlist.objects.all()    
    read = {'blog':blogs, 'randomBlogs': randomBlogs, 'playlist': playlist}
    return render(request, 'blogs/readblogs.html', read)


def TagsBlog(request, id=id):
    tag = AddBlog.tags.get(id=id)
    return render(request, 'blogs/tagsblog.html', {'tags': tag})


def ReadPlay(request, post_id):
    plays = Playlist.objects.get(pk = post_id)
    blogs = AddBlog.objects.filter(play=plays)
    read = {'blogs':blogs, 'play':plays}
    return render(request, "blogs/read_play.html", read)


