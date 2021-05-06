from django.shortcuts import render

from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def home(request):
    print("inside home view--------------")
    return HttpResponse("I am Home")

def greet(request):
    print("greet response")
    return HttpResponse("Hello ABC Greetings.....")


def function(request):
    print("i am inside function ")
    return render(request, 'home.html', context={"msg" : "Hello World..."})

def exception(request):
    # try:
    #     ans = 15/0
        # print(ans)
    # except ZeroDivisionError("can not devide by zero.....")
    # div = 15/0
    # print([1,2,3][3])
    print(15/0)
    return HttpResponse(ZeroDivisionError("can not devide by zero....."))


def temp_response(request):
    print("in template response......")
    context = {"name" : "Tejashree", "lastname" : "P"}
    # return render(request, template_name = 'temp.html', context = context)     # when not using    process_template_response   in HooksMiddleware
    return TemplateResponse(request, template = 'temp.html', context = context)     # when using   process_template_response   in HooksMiddleware