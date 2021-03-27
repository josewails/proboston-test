from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import CompanyForm


class HomeView(View):

    @staticmethod
    def get(request):
        context = dict(form=CompanyForm())
        return render(request, "companies/home.html", context=context)

    @staticmethod
    def post(request):
        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse(dict(message="Record added successfully", success=True))

        else:
            context = dict(form=form)
            html_form = render_to_string("companies/form.html", context=context, request=request)
            return JsonResponse(dict(htmlForm=html_form, success=False))
