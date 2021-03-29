from django.shortcuts import render

# Create your views here.


def store(request):
    context = {}
    return render(request, 'templates/store/Store.html', context)
