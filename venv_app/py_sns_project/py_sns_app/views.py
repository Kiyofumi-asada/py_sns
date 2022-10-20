from django.shortcuts import render
#models
from .models import Post

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
  detailData = Post.objects.get(slug=slug)
  return render(request, "post_detail.html", {"detail": detailData})