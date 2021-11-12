from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd
# Create your views here.

def home(request):
   return render(request, 'home/welcome.html') 

        
def about(request):
    return render(request, 'home/about.html')
