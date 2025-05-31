from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CarListView(ListView):
  model = Car
  template_name = 'cars.html'
  context_object_name = 'cars'

  def get_queryset(self):
    cars = super().get_queryset().order_by('model')
    search = self.request.GET.get('search')
    if search:
      cars = Car.objects.filter(model__icontains = search)
    return cars
  
class carDetailView(DetailView):
  model = Car
  template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class newCarCreateView(CreateView):
  model = Car
  form_class = CarModelForm
  template_name = 'new_car.html'
  sucess_url = '/cars/'

  def get_success_url(self):
    return reverse_lazy('car_detail', kwargs={'pk', self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class carUpdateView(UpdateView):
  model = Car
  form_class = CarModelForm
  template_name = 'car_update.html' 
  success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class carDeleteView(DeleteView):
  model = Car
  template_name = 'car_delete.html'
  success_url = '/cars/'