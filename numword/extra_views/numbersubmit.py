from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.template import loader
from djangojs import views

from numword import intercool_require


class SearchSubmitView(View):
    template = 'result_display.html'
    response_message = 'This is the response'

    def post(self, request):
        template = loader.get_template(self.template)
        query = request.POST.get('number', '')

        # A simple query for Item objects whose title contain 'query'
        items = intercool_require.convert(request)
        context = items

        rendered_template = template.render(context, request)
        return HttpResponse(rendered_template, content_type='text/html')