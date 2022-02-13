import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
import geopandas
from shapely.geometry import Polygon
from django.views.generic import View
areas = geopandas.read_file("bgdensity/bulgaria.shp")

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'baseProfile.html')
    else:
        return redirect("/login_menu/")

def logout_view(request):
    logout(request)
    return redirect('/')

def delete(request):
    User.objects.get(username = request.user.username).delete()
    return redirect("/")

def overlap(poly1, selected):
    # selected = (24.26911, 43.02215), (26.57979, 43.02215), (26.57979, 42.01308), (24.26911, 42.01308)
    poly2 = Polygon(selected)
    overlapping_area = poly1.intersection(poly2).area 
    return overlapping_area

def ajax(selected):  
    population = 0
    #city = areas.loc[areas["LAU_NAME"] == name]
    for city in areas.iloc:
        overlaping_area = overlap(city.geometry, selected)
        if(overlaping_area > 0):
            overlaping_area = city.geometry.area / overlaping_area
            km = city.AREA_KM2 /overlaping_area
        else:
            km = 0
        population += city.POP_DENS_2 * km
    return round(population)

class AjaxView(View):
    def get(self, request):
        ymin = float(request.GET.get('ymin'))
        ymax = float(request.GET.get('ymax'))
        xmin = float(request.GET.get('xmin'))
        xmax = float(request.GET.get('xmax'))
        selected = (xmin, ymax), (xmax, ymax), (xmax, ymin), (xmin, ymin)
        population = ajax(selected)

        return JsonResponse({'info' : population})