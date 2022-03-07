from turtle import numinput
from django.http import HttpResponseRedirect
import json
from re import template
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
import geopandas
from matplotlib.style import context
from shapely.geometry import Point
from shapely.geometry import Polygon
from django.views.generic import View
from .utils.mixins import Permissions, News
from django.contrib.auth.models import Group
areas = geopandas.read_file("bgdensity/bulgaria.shp")

class ProfileView(Permissions, News):
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
    try:
        population = 0
        for city in areas.iloc:
            area_population = 0
            meter = 0
            if city.settleme_3:
                overlaping_area = overlap(city.geometry, selected)
                if(overlaping_area > 0):
                    overlaping_area = city.geometry.area / overlaping_area
                    meter = float(city.settleme_3) / float(overlaping_area)
                    area_population = float(city.settleme_4) / float(city.settleme_3) 
                
            population += area_population * meter
        return round(population)
    except Exception as ex:
        return "population error: "+ ex
def take_business(selected, amenity):
    try:
        business = []
        with open('bgdensity/'+amenity+'DB.json', encoding="utf8") as file:
            templates = json.load(file)['elements']
            for i in templates:
                valid_type = i.get('type', False) == 'node'
                valid_param = i.get('tags', False)
                if all([valid_type, valid_param]):
                    point = Point(i['lon'], i['lat'])
                    if selected.contains(point):
                        business.append(i['tags'])
        return business
    except Exception as ex:
        return "business error: "+ex

class AjaxView(Permissions):
    
    def get(self, request):
        try:
            context = self.get_context_data()
            coordinates = request.GET.get('data', None)
            amenity = request.GET.get('type', None)
            selected = Polygon(json.loads(coordinates))
            population = ajax(selected)
            business = "NO ACCESS, PLS BUY"
            
            if not context.get("is_free", False):
                business = take_business(selected, amenity)
            
            data = {'population' : population,'business' : business}

        except Exception as ex:
            data = {"error":str(ex)}
            
        return JsonResponse(data)
