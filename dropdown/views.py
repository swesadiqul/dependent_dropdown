from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import *

# class SubDistrictListView(ListView):
#     model = SubDistrict
#     context_object_name = 'subdistrict'

class AreaCreateView(CreateView):
    model = Area
    form_class = AreaForm
    success_url = '/thanks/'

# class SubDistrictUpdateView(UpdateView):
#     model = SubDistrict
#     form_class = SubDistrictForm
#     success_url = reverse_lazy('subdistrict_changelist')


def load_districts(request):
    division_id = request.GET.get('division')
    districts = District.objects.filter(division_id=division_id).order_by('name')
    return render(request, 'dropdown/district_dropdown_list_options.html', {'districts': districts})


def load_subdistricts(request):
    district_id = request.GET.get('district')
    subdistricts = SubDistrict.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'dropdown/subdistrict_dropdown_list_options.html', {'subdistricts': subdistricts})