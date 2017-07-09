from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm, formset_factory
from rest_framework import viewsets
from rest_framework.decorators import detail_route

from .models import Customer, Product, Rent, RentDetail
from .serializers import CustomerSerializer, ProductSerializer


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = ['customer', 'happen_date']


class RentDetailForm(ModelForm):
    class Meta:
        model = RentDetail
        fields = ['product', 'count']


RentDetailFormSet = formset_factory(RentDetailForm, extra=2, can_delete=True)


def index(request):
    return HttpResponse('Hello, world, you are at the rents index.')


def add(request):
    if request.method == 'GET':
        context = {
            "form": RentForm(),
            "formset": RentDetailFormSet,
        }
        return render(request, 'rents/add.html', context)

    if request.method == 'POST':
        form = RentForm(request.POST)
        print(request.POST)
        if form.is_valid():
            return HttpResponse('add rent successful.')
        else:
            return HttpResponse('add rent failed.')


def change(request, rent_id):
    context = {}
    return render(request, 'rents/change.html', context)
