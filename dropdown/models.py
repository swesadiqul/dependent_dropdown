from django.db import models

class Division(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Division'

class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'District'

class SubDistrict(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Sub District'


class Area(models.Model):
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    sub_district = models.ForeignKey(SubDistrict, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.division.name + ", " + self.district.name + ", " + self.sub_district.name
    
    class Meta:
        verbose_name_plural = 'Area'