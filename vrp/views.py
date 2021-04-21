from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CitySerializer

from .models import City
from .tsp import GeneticAlgo, get_distance
import math
# Create your views here.
@api_view(['GET'])
def results(request):
		# cities = """
	# Grenoble
	# Lyon
	# Bourgoin jallieu
	# Chambery
	# Annecy
	# Thonon-les-Bains
	# Aix-les-bains
	# Voiron
	# Annemasse
	# Évian-les-Bains
	# """
	# dd="""
	# Villard-de-Lans
	# Saint-Pierre-de-Chartreuse
	# La tour du pin
	# Beaurepaire
	# Rumily
	# Échirolles
	# Voreppe
	# Allevard
	# La mure
	# Vizille
	# Vienne
	# Le touvet
	# La tronche
	# Moirans
	# Seyssins
	# """
	# cities = input()
	conversion_factor = 0.62137119 

	#citiess = City.objects.all()
	#print(" here  ", citiess)
	noms = City.objects.values_list('title', flat=True)
	cities = list(noms)
	# cities = [c for c in cities.split('\n') if c != '']
	#cities = ['Grenoble', 'Lyon', 'Bourgoin jallieu', 'Chambery', 'Annecy', 'Thonon-les-Bains', 'Aix-les-bains', 'Voiron', 'Annemasse', 'Évian-les-Bains' ]
	#cities = ['Grenoble', 'Lyon', 'Bourgoin jallieu', 'Chambery', 'Annecy']
	print("cities", cities)
	edges = []
	dist_dict = {c:{} for c in cities}
	for idx_1 in range(0,len(cities)-1):
		for idx_2 in range(idx_1+1,len(cities)):
			city_a = cities[idx_1]
			city_b = cities[idx_2]
			dist = get_distance(city_a,city_b)
			print(int(dist/conversion_factor))
			dist_dict[city_a][city_b] = dist/conversion_factor
			edges.append((city_a,city_b,dist))

	g = GeneticAlgo(hash_map=dist_dict,start='Grenoble',mutation_prob=0.25,crossover_prob=0.25,population_size=len(cities)+1,steps=15,iterations=2000)
	print("resultas ", g.converge())
	resultats =  g.converge()
	count = 1
	for city in resultats:
		if(city != 'Grenoble'):
			print("city1", city)
			ville=City.objects.get(title=city)
			print("ville ", ville)
			ville.priority=count
			ville.save()
			count = count+1

	# nb = len(cities)
	# print ("nombre de villes ", nb)
	# print("nombre de routes possibles : ", math.factorial(nb))
	cities = City.objects.all().order_by('-priority')
	print("cities", cities)
	serializer = CitySerializer(cities, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def apiOverview(request):
	vrp_urls = {
		'List':'/city-list/',
		'Results':'results',
		'Detail View':'/city-detail/<str:pk>/',
		'Create':'/city-create/',
		'Update':'/city-update/<str:pk>/',
		'Delete':'/city-delete/<str:pk>/',
		}

	return Response(vrp_urls)

@api_view(['GET'])
def cityList(request):
	cities = City.objects.all().order_by('-id')
	serializer = CitySerializer(cities, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def cityDetail(request, pk):
	cities = City.objects.get(id=pk)
	serializer = CitySerializer(cities, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def cityCreate(request):
	serializer = CitySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def cityUpdate(request, pk):


	city = City.objects.get(id=pk)
	serializer = CitySerializer(instance=city, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def cityDelete(request, pk):
	city = City.objects.get(id=pk)
	city.delete()

	return Response('Item succsesfully delete!')

# Create your views here.
