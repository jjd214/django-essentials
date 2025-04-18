import random
from django.shortcuts import render
from visits.models import Visit

# Create your views here.
def index(request, get_page=""):
    visit = Visit(page=get_page)
    if request.user.is_authenticated:
        visit.username = request.user.username
    visit.save()
    visitors = Visit.objects.filter(page=get_page)
    context = {
        "nums_of_visits": visitors.count,
        "page": get_page,
        "visitors": visitors,
    }
    return render(request, 'index.html', context=context)