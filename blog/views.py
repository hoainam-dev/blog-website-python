from django.shortcuts import render, get_object_or_404

from .models import Post

def blog(request):
    data = {"Posts": Post.objects.all().order_by("-date")}
    return render(request,'pages/blog.html', data)

def post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    data = {"Datas": Post.objects.all().order_by("-date")}
    return render(request, "pages/post.html", {"post":post, "data":data})