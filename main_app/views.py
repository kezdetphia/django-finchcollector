from django.shortcuts import render

# Create your views here.

finches = [
    {'name': 'House Finch', 'color': 'blue'},
    {'name': 'American Goldfinch', 'color': 'gold'},
    {'name': 'European Goldfinch', 'color': 'yellow'},
    {'name': 'Purple Finch', 'color': 'purple'},

]



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html' , {
        'finches': finches
    })