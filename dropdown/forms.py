from django import forms
from .models import *

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('division', 'district', 'sub_district')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.none()
        self.fields['sub_district'].queryset = SubDistrict.objects.none()

        if 'division' in self.data:
            try:
                division_id = int(self.data.get('division'))
                # district_id = int(self.data.get('sub_district'))
                self.fields['district'].queryset = District.objects.filter(division_id=division_id).order_by('name')
                # self.fields['sub_district'].queryset = SubDistrict.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.division.district_set.order_by('name')
            # self.fields['sub_district'].queryset = self.instance.district.sub_district_set.order_by('name')


        if 'district' in self.data:
            try:
                # division_id = int(self.data.get('division'))
                district_id = int(self.data.get('district'))
                # self.fields['district'].queryset = District.objects.filter(division_id=division_id).order_by('name')
                self.fields['sub_district'].queryset = SubDistrict.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            # self.fields['district'].queryset = self.instance.division.district_set.order_by('name')
            self.fields['sub_district'].queryset = self.instance.district.sub_district_set.order_by('name')