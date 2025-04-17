import random
from django.shortcuts import render
from visits.models import Visits

# Create your views here.
def index(request):
    visits = Visits.objects.first()
    visits.count += 1
    visits.save()
    context = {
        "nums_of_visits": visits.count
    }
    return render(request, 'index.html', context=context)