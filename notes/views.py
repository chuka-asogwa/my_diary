from django.shortcuts import render

def index(request):
    """ Home page for My Diary """
    return render(request, 'notes/index.html')



    
