from django.shortcuts import render
from django.http import HttpResponse
from nwr_app.models import temp_input_form
from nwr_app.nwr_model import convert_temp

def index(request):
    if request.method == 'POST':
        form = temp_input_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)
    else:
        form = temp_input_form()

    return render(request, 'nwr_app/index.html', {'form': form})

def present_output(form):
    cel_input = form.cel_input
    s = convert_temp(cel_input)
    return HttpResponse('Degree conversion function: Fahrenheit(%s C) = %s F' % (cel_input, s))
