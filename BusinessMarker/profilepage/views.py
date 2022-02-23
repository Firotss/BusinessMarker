from django.http import HttpResponseRedirect
import json
from re import template
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
import geopandas
from shapely.geometry import Point
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

def take_business(selected, amenity):
    business = []
    with open('bgdensity/'+amenity+'DB.json', encoding="utf8") as file:
        templates = json.load(file)['elements']
        try:
            for i in templates:
                point = Point(i['lon'], i['lat'])
                if selected.contains(point):
                    business.append(i['tags'])
        except:
            print("true")
    return business

class AjaxView(Permissions):
    
    def get(self, request):
        try:
            coordinates = request.GET.get('data', None)
            amenity = request.GET.get('type', None)
            selected = Polygon(json.loads(coordinates))
            population = ajax(selected)
            business = take_business(selected, amenity)
            data = {'population' : population,'business' : business}

        except Exception as ex:
            print(ex)
            data = {"error":ex}

        return JsonResponse(data)
