from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class ProcessRequestMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print(request.META.get('HTTP_CSRFTOKEN'))
        print(request.META.get('HTTP_SESSIONID'))
        user = request.user
        if not user.is_authenticated:
            return HttpResponse('Unauthorised', status=401)