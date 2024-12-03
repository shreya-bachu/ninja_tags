from django.shortcuts import render

def jinja_print(request):
    d={'name':'shreya','age':'21'}
    return render(request,'jinja_print.html',context=d)

# Create your views here.
