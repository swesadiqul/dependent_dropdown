from django.urls import path

from . import views

urlpatterns = [
    # path('', views.SubDistrictListView.as_view(), name='subdistrict_changelist'),
    path('', views.AreaCreateView.as_view(), name='area_add'),
    # path('<int:pk>/', views.SubDistrictUpdateView.as_view(), name='subdistrict_change'),


    path('ajax/load_districts/', views.load_districts, name='ajax_load_districts'),  # <-- this one here
    path('ajax/load_subdistricts/', views.load_subdistricts, name='ajax_load_subdistricts'),  # <-- this one here
]