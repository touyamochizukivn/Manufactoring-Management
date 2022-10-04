from django.shortcuts import render
import pandas as pd
from plotly.offline import plot
import plotly.express as px

from core.forms import *


def dashboard(request):
    return render(request, 'dashboard.html')

def component_add(request):
    if request.method == 'POST':
        form = ComponentAdd(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ComponentAdd()
    return render(request, 'component/add.html', {'form': form})

def supplier_add(request):
    if request.method == 'POST':
        form = SupplierAdd(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupplierAdd()
    return render(request, 'supplier/add.html', {'form': form})


def test(request):
    qs = Plan.objects.all()
    project_data = [
        {
            'Plan': x.name,
            'Start': x.start_date,
            'Finish': x.end_date,
            'Responsible': x.responsible
        }for x in qs 
    ]

    df = pd.DataFrame(project_data)
    print(df)

    fig = px.timeline(df, x_start="Start", x_end="Finish" ,y="Plan", color="Responsible"
    )

    fig.update_yaxes(autorange="reversed") # for data in chart to appear in reversed order
    gantt_plot = plot(fig, output_type="div")
    context ={'plot_div':gantt_plot}
    return render(request, 'test.html',context)