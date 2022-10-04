

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse



from django.shortcuts import render, redirect
from .models import *
# from .aigenerator import *
from .functions import *
from .customFunctions import *
from django.contrib import messages
from django.conf import settings
import datetime

###########################
# OPENAI SECTION
###########################

def openai_home(request):
    context = {'segment': 'home'}

   

    if request.method == 'POST':
        businessName = request.POST['businessName']
        businessDo = request.POST['businessDo']


        context['businessName'] = businessName
        context['businessDo'] = businessDo
        try:
            context['section1Title'] = returnSection1Title(businessDo)
            context['section1Description'] = getDescription(businessName, businessDo, 265)

            #Get The Service Titles
            services = []
            
            serviceTitles = return3Services(businessDo)
            for service in serviceTitles:
                obj = {}
                serviceDescription = returnServiceDescription(service)
                try:
                    obj['title'] = service.strip()
                except:
                    obj['title'] = service
                try:
                    obj['description'] = serviceDescription.strip()
                except:
                    obj['description'] = serviceDescription
                services.append(obj)

            #Get The Feature Titles
            features = []
            featureTitles = return3Features(businessDo)
            for feature in featureTitles:
                obj = {}
            
                featureDescription = returnFeatureDescription(feature)
            
                try: obj['title'] = feature.strip()
                except: obj['title'] = feature
                try: obj['description'] = featureDescription.strip()
                except: obj['description'] = featureDescription
                features.append(obj)


            context['service1Title'] = services[0]['title']
            context['service1Description'] = services[0]['description']
            context['service2Title'] = services[1]['title']
            context['service2Description'] = services[1]['description']
            context['service3Title'] = services[2]['title']
            context['service3Description'] = services[2]['description']

            context['section3Title'] = returnSection1Title(businessDo)
            context['section3Description'] = getDescription(businessName, businessDo, 265)

            context['features1Title'] = features[0]['title']
            context['features1Description'] = features[0]['description']
            context['features2Title'] = features[1]['title']
            context['features2Description'] = features[1]['description']
            context['features3Title'] = features[2]['title']
            context['features3Description'] = features[2]['description']
            return render(request, 'openai/openai_result_generator.html', context)
        except: context['businessName'] = 'Sorry Open AI KEY NOT AVAILABLE'
            
    return render(request, 'openai/openai_page.html', context)

def openai_Web(request):
    context = {}
    html_template = loader.get_template('landing/login.html')
    return HttpResponse(html_template.render(context, request))


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


###########################
# ZOOM WEATHER SECTION
###########################



def weather_home(request):
    context = {'segment': 'weather home'}

   
    context['TODAY'] = datetime.datetime.now()
    print(datetime.datetime.now())
    if request.method == 'POST':
        businessName = request.POST['businessName']
        businessDo = request.POST['businessDo']
            
    return render(request, 'projects/weather/weather_home.html', context)

## API WEATHER CALL 
def StormResponse(request):
    context = {}
    FROM = '2000-01-01T18:00Z'
    TO = '2022-01-01T18:00Z'
    if request.method == 'POST':
        FROM = request.POST['FROM']
        TO = request.POST['TO']
        print(FROM, TO)
        context['RESPONSE'] = returnStorm(FROM+'T18:00Z', TO+'T18:00Z')
            
    return JsonResponse(context)