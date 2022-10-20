from django.shortcuts import render

# Create your views here.

# root(/)
def topPage(request):
  print("==========views:TopPage==========")
  return render(request,"top.html")