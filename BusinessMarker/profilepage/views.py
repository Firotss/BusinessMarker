from django.http import HttpResponseRedirect
import json
from re import template
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
import geopandas
from shapely.geometry import Polygon
from django.views.generic import View
from .utils.mixins import Permissions
areas = geopandas.read_file("bgdensity/bulgaria.shp")

class ProfileView(Permissions):
    template_name = "baseProfile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['redirect'] = HttpResponseRedirect('/')
        return context

def logout_view(request):
    logout(request)
    return redirect('/')

def delete(request):
    User.objects.get(username = request.user.username).delete()
    return redirect("/")

def overlap(poly1, selected):
    poly2 = Polygon(selected)
    overlapping_area = poly1.intersection(poly2).area 
    return overlapping_area

def ajax(selected):  
    population = 0
    for city in areas.iloc:
        overlaping_area = overlap(city.geometry, selected)
        if(overlaping_area > 0):
            overlaping_area = city.geometry.area / overlaping_area
            km = city.AREA_KM2 /overlaping_area
        else:
            km = 0
        population += city.POP_DENS_2 * km
    return round(population)

class AjaxView(Permissions):
    
    def get(self, request):
        try:
            ymin = float(request.GET.get('ymin'))
            ymax = float(request.GET.get('ymax'))
            xmin = float(request.GET.get('xmin'))
            xmax = float(request.GET.get('xmax'))
            selected = (xmin, ymax), (xmax, ymax), (xmax, ymin), (xmin, ymin)
            # mapcoordinates = ['xmin', 'xmax', 'ymin', 'ymax']
            # cleaned_values = {c: float(request.GET.get(c)) for c in self.mapcoordinates}
            # from_request = '%(xmin)f,%(ymax)f,%(xmax)f,%(ymax)f,%(xmax)f,%(ymin)f,%(xmin)f,%(ymax)f' % cleaned_values
            
            # coordinates = [float(i) for i in from_request.split(',')]
            # selected = tuple(zip(*[iter(coordinates)] * 2))
            # print(selected)
            population = ajax(selected)
            data = {'population' : population}

        except Exception as ex:
            data = {"error":"wrong data"}

        return JsonResponse(data)