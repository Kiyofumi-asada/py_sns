from django.shortcuts import render, redirect
from .models import Post
from py_sns_app.forms import CommentForm

# Create your views here.

# root(/)
def topPage(request):
  print("==========TopPage==========")
  # read
  data = Post.objects.all()
  return render(request, "top.html", {"posts": data})

# postDetail(/slug)
def postDetail(request, slug):
  print("==========PostDetailPage:",slug,"==========")
  # read detail
  post = Post.objects.get(slug=slug)
  if request.method == "POST":
    form = CommentForm(request.POST)
    print("form",form)
    print("form.is_valid",form.is_valid())
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
      print("comment",comment)
      return redirect("postDetail", slug=post.slug)
  else:
    form=CommentForm()
    print("form",form)
  return render(request, "post_detail.html", {"post": post, "form":form})