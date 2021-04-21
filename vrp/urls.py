from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('city-list/', views.cityList, name="city-list"),
	path('results/', views.results, name="results"),
	path('city-detail/<str:pk>/', views.cityDetail, name="city-detail"),
	path('city-create/', views.cityCreate, name="city-create"),

	path('city-update/<str:pk>/', views.cityUpdate, name="city-update"),
	path('city-delete/<str:pk>/', views.cityDelete, name="city-delete"),
]