from django.shortcuts import render, redirect
from .models import Post
from py_sns_app.forms import PostForm, CommentForm

# Create your views here.

# top(/)
def topPage(request):
  print("==========TopPage==========")
  # read
  data = Post.objects.all()
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      data = form.save(commit=False)
      data.post = data
      data.save()
      return redirect("topPage")
  else:
    form=PostForm()
  return render(request, "top.html", {"posts": data, "form":form})

# postDetail(/slug)
def postDetail(request, slug):
  print("==========PostDetailPage:",slug,"==========")
  # read detail
  post = Post.objects.get(slug=slug)
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      data = form.save(commit=False)
      data.post = post
      data.save()
      return redirect("postDetail", slug=post.slug)
  else:
    form=CommentForm()
  return render(request, "post_detail.html", {"post": post, "form":form})