from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'url_template/index.html')

def other(request):
    return render(request, 'url_template/other.html')

def relative(request):
    return render(request, 'url_template/relative_url_template.html')
