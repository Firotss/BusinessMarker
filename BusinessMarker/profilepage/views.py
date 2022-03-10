from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from shapely.geometry import Point
from shapely.geometry import Polygon
from bs4 import BeautifulSoup
from .utils.mixins import Permissions, News
import geopandas
import json
import requests as req
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
                try:
                    overlaping_area = overlap(city.geometry, selected)
                    if(overlaping_area > 0):
                        overlaping_area = city.geometry.area / overlaping_area
                        meter = float(city.settleme_3) / float(overlaping_area)
                        if city.settleme_3 != "0" and city.settleme_4 != "0":
                            area_population = float(city.settleme_4) / float(city.settleme_3) 
                except Exception as ex:
                    print(ex)
                
            population += area_population * meter
        return round(population)
    except Exception as ex:
        return "population error: "+ ex
def take_business(selected, amenity, source):
    try:
        if source == "api":
            coordinates = []
            for item in selected.bounds:
                coordinates.append(str(item))
            print(amenity)
            url = "https://lz4.overpass-api.de/api/interpreter?data=[bbox];node[amenity="+amenity+"];out;&bbox="+coordinates[0]+","+coordinates[1]+","+coordinates[2]+","+coordinates[3]
            resp = req.get(url)
            soup = BeautifulSoup(resp.text, 'lxml')
            business = []
            elements = soup.find_all('node')
            for element in elements:
                local_element = {}
                items = element.find_all('tag')
                for item in items:
                    local_element[item['k']] = item['v']    
                business.append(local_element)
            return business
        else:
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
        print(ex)
        return "business error: "+ex

class AjaxView(Permissions):
    
    def get(self, request):
        try:
            context = self.get_context_data()
            coordinates = request.GET.get('data', None)
            amenity = request.GET.get('type', None)
            source = request.GET.get('source', None)
            
            selected = Polygon(json.loads(coordinates))
            population = ajax(selected)
            business = "NO ACCESS, PLS BUY"

            if not context.get("is_free", False):
                business = take_business(selected, amenity, source)
            
            data = {'population' : population,'business' : business}
            
        except Exception as ex:
            data = {"error":ex}
            
        return JsonResponse(data)
