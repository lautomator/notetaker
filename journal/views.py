from django.shortcuts import render

def index(request):
    context = {
        'date': '20220910',
    }
    return render(request, 'journal/index.html', context)
