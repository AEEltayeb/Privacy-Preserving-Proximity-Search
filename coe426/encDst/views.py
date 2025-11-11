import math
from django.shortcuts import render
from .utils import populate_locations, encrypt_diffs
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from phe import paillier
import random
from .models import Location
from django.http import HttpResponse

def main(request):
    if not Location.objects.exists():
        populate_locations()  # Populate the Location table if it's empty
    return render(request, 'index.html')
    
def dst(request):
    x_value = request.GET.get('x', '')  # Retrieve the value of 'x'
    y_value = request.GET.get('y', '')  # Retrieve the value of 'y'
    top_activities = encrypt_diffs(x_value, y_value)

    # Redirect or render your response
    return render(request, 'results.html', {'top_activities': top_activities})

