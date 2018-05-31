from django.http import QueryDict, HttpResponse
from django.utils.deprecation import MiddlewareMixin
 
class HttpPostTunnelingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        
        #Checks if the header contains an override
        #If you use the common.js ajax helper functions for
        #PUT and DELETE, it will contain this.
        if request.META.get('HTTP_METHODOVERRIDE', False):
            http_method = request.META['HTTP_METHODOVERRIDE']

            #Check if it's a PUT and sets the method
            if http_method.lower() == 'put':
                request.method = 'PUT'
                request.META['REQUEST_METHOD'] = 'PUT'
                request.PUT = QueryDict(request.body)

            #Checks if it's a DELETE and sets it as so
            if http_method.lower() == 'delete':
                request.method = 'DELETE'
                request.META['REQUEST_METHOD'] = 'DELETE'
                request.DELETE = QueryDict(request.body)
        return None

    def process_exception(self, request, exception):
        return HttpResponse("Unable to process request.")
