import re
from django.conf import settings
from django.shortcuts import redirect

EXEMPT_URLS = [re.compile(settings.LOGIN_URL)]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

###################******"CALLED DURING REQUEST"*******###############################

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info
        print(path)

        if not request.user.is_authenticated:
            if not any(url.match(path)for url in EXEMPT_URLS):
                return redirect(settings.LOGIN_URL)

    """
    called just before django calls the view
    Return either None or HttpResponse
    """

    def process_request(request):
        """
                :return:
        """
####################****"CALLED DURING RESPONSE"*****###################################

    def process_exception(self, request, exception):
        '''

        :param request:
        :param exception:
        called for the response if the exception is raised by te view
        Return either None or HttpResponse
        '''

    def process_template_response(self,request, response):
        """

        :param request:
        :param response:
        request - HttpRequestObject
        response - TemplateResponseObject
        return templateResponse
        use this for changing template or context if it is needed.
        """

    def process_response(request, response):
        """

        :param response:
        :return:
        """