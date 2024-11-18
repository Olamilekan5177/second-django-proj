from django.shortcuts import render

# Create your views here.
def Error404 (request):
  return render(request, 'App/Error404.html')

def about (request):
  return render(request, 'App/about.html')

def base (request):
  return render(request, 'App/base.html')

def cart (request):
  return render(request, 'App/cart.html')

def checkout(request):
  return render(request, 'App/cart.html')

def contact(request):
  return render(request, 'App/contact.html')

def index (request):
  return render(request, 'App/index.html')

def index_2(request):
  return render(request, 'App/index_2.html')

def news(request):
  return render(request, 'App/news.html')

def shop(request):
  return render(request, 'App/shop.html')

def single_news(request):
  return render(request, 'App/single-news.html')

def single_product(request):
  return render(request, 'App/single-product.html')



