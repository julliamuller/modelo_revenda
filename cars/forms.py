from django import forms
from cars.models import Brand, Car

class CarForm (forms.Form):
  model = forms.CharField(max_length=200)
  brand = forms.ModelChoiceField(Brand.objects.all())
  factor_year = forms.IntegerField()
  plate = forms.CharField(max_length=10)
  value = forms.FloatField()
  photo = forms.ImageField()

  def save(self):
    car = Car(
      model = self.cleaned_data['model'],
      brand = self.cleaned_data['brand'],
      factor_year = self.cleaned_data['factor_year'],
      plate = self.cleaned_data['plate'],
      value = self.cleaned_data['value'],
      photo = self.cleaned_data['photo']
    )
    car.save()
    return car
  
class CarModelForm (forms.ModelForm):
  class Meta:
    model = Car
    fields = '__all__'

  def clean_value(self):
    value = self.cleaned_data.get('value')
    if value < 20000:
      self.add_error('value', 'Valor mínimo deve ser R$20.000,00') 
    return value
