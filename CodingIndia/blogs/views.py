from django.shortcuts import render, redirect
from blogs.forms import *
from blogs.models import AddBlog, Playlist, SomeModel
from django.views.decorators.cache import cache_page

######################## Views ##################################
@cache_page(60 * 15)
def index(request):
    blogs = AddBlog.objects.all()
    play = Playlist.objects.all()
    ran = AddBlog.objects.order_by('?')[0]
    print("Ran: ", ran)
    # print("Ran: ", ran)

    # tags = AddBlog.tags.all()
    context = {'blogs':blogs, 'ran': ran, 'play':play}
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


from django.http import FileResponse, Http404
from django.http import HttpResponse
from django.conf import settings
import os

@cache_page(60 * 15)
def download_image(request, image_path):
    full_path = os.path.join(settings.MEDIA_ROOT, image_path)
    if os.path.exists(full_path):
        with open(full_path, 'rb') as image_file:
            response = FileResponse(image_file)
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(full_path)}"'
            return response
    else:
        raise Http404("Image not found")
    

@cache_page(60 * 15)
def Readblog(request, post_id):
    blogs = AddBlog.objects.get(pk = post_id)
    img_url = blogs.img.url
    
    print("Img Url: ", img_url)
    
    try:
        response = download_image(request, img_url)
        return response
    except Http404 as e:
        # Handle the case when the image is not found
        return HttpResponse(str(e), status=404)
    
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


