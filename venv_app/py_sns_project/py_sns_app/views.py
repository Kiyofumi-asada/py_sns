from django.shortcuts import render
#models
from .models import Post

# Create your views here.

# root(/)
def topPage(request):
  print("==========views:TopPage==========")
  # read
  read = Post.objects.all()
  return render(request, "top.html", {"posts": read})