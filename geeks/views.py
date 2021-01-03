
from django.shortcuts import render 
from .forms import GeeksForm 
  
# Create your views here. 
def home_view(request): 
    context = {}
    form = GeeksForm(request.POST or None) 
    context['form']= form 
    if request.POST: 
        if form.is_valid(): 
            temp = form.cleaned_data.get("geeks_field") 
            context = { 'temp': temp }
            Weight1 = temp

            pounds = Weight1 * 0.45
            context = { 'temp': temp,
            'pounds': pounds }

            kilos = Weight1 / 0.45
            context = { 'temp': temp,
            'pounds': pounds,
            'kilos': kilos }
            
            if 'pounds-con' in request.POST:
                context = { 
            'temp': temp,
            'weight': pounds,
            'pounds': pounds,
            'kilos': kilos,
            'visible': True,
            'visible2': False }

            if 'kilos-con' in request.POST:
                context = { 
            'temp': temp,
            'weight': kilos,
            'pounds': pounds,
            'kilos': kilos,
            'visible': False,
            'visible2': True }

    return render( request, "blog/weight.html", context)
