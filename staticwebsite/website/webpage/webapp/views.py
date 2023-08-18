from django.shortcuts import render
from . models import Place
from . models import Names
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obje=Names.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obje})