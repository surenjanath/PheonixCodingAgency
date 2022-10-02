

from django.shortcuts import render, redirect
from .models import *
from .functions import *
from django.contrib import messages
from django.conf import settings
import time

###########################
# LANDING PAGE SECTION
###########################

def payroll_home(request):
    context = {'segment': 'home'}

   

    if request.method == 'POST':
        pass
    return render(request, 'group_project/payroll/index.html', context)


# # @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('landing/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('landing/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('landing/page-500.html')
#         return HttpResponse(html_template.render(context, request))
