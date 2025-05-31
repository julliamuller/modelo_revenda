from django.contrib import admin
from cars.models import Car, Brand

class carAdmin(admin.ModelAdmin):
  list_display = ('model','brand','factor_year', 'model_year', 'value')
  search_fields = ('model', 'brand')

class BrandAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',) 

admin.site.register(Car, carAdmin)
admin.site.register(Brand, BrandAdmin)