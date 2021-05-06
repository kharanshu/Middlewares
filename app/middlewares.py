from django.http import HttpResponse

def Fun_middleware(get_response):
    print("Congratulations....middleware Function Initialization")  # will be called right after runserver

    def inner_middleware(request):
        print("Before calling view")
        response = get_response(request)
        print("After calling view")
        return response
    return inner_middleware


class MumbaiMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("Congratulations, Initialization --- class Mumbai")    # 3

    def __call__(self, request):
        print("Before calling view, ***** Mumbai")      #5
        response = self.get_response(request)       # ref of Delhi_middleware
        print("After calling view, ***** Mumbai")      # 10
        return response

class DelhiMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("Congratulations, Initialization ***** class Delhi")     # 2

    def __call__(self, request):
        print("Before calling view, ***** Delhi")      # 6
        response = self.get_response(request)       # Chennai_middleware ref
        print("After calling view, ***** Delhi")      # 9
        return response

class ChennaiMiddlewares:

    def __init__(self, get_response):
        self.get_response = get_response
        print("Congratulations, Initialization ***** class Chennai")     # 1

    def __call__(self, request):
        print("Before calling view, ***** Chennai")      # 7
        response = self.get_response(request)       # Actual View from views.py
        print("After calling view, ***** Chennai")      # 8
        return response

class Hooks:

    def __init__(self, get_response):
        self.get_response = get_response
        print("Configuration, Initalization --- class Hook")      # 1

    def __call__(self, request):
        print("Before claaling view --- HOOKS")      # 7
        response = self.get_response(request) 
        # print(response.content, "view response")     # view
        print("After claaling view ---  HOOKS")      # 8
        return response

    def process_template_response(self, request, response):
        print(response.context_data)
        response.context_data['name'] = 'ABC'        # updating context, name from views.py
        response.context_data['lastname'] = 'XYZ'
        translations = {
            "en" : {"greeting" : "Hello", "header" : "Welcome Django!"},
            "nl" : {"greeting" : "Hallo", "header" : "Welkom Django!"}
        }

        response.context_data['translation'] = translations
        print("in Template Process --- middleware part ")
        return response


