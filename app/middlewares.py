def my_middleware(get_response):
    print("Configuration...!")
    def inner_mw(request):
        print("Before call view")
        response = get_response(request)
        print("After calling View")
        return response
    return inner_mw


class MumbaiMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Configurations...!---- Mumbai")

    def __call__(self, request):
        print("Before calling view -- in Mumbai method")
        response = self.get_response(request)
        print("After calling view -- in Mumbai method")
        return response
    
class DelhiMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Configurations...! ---- Delhi")

    def __call__(self, request):
        print("Before calling view -- in Delhi method")
        response = self.get_response(request)
        print(response.content, "In Noida")
        print("After calling view -- in Delhi method")
        return response

class NoidaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Configurations...! ---- Noida")

    def __call__(self, request):
        print("Before calling view -- in Noida method")
        response = self.get_response(request)
        print(response.content, "In Noida")
        print("After calling view -- in Noida method")
        return response
     