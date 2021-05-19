from django.shortcuts import render

# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def prazna_stran(request):
    return render(request, 'blog/prazna.html', {})