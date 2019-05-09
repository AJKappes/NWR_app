from django.shortcuts import render
from django.http import HttpResponse
#from nwr_app.models import temp_input_form
#from nwr_app.nwr_model import convert_temp
from nwr_app.models import pdf_input_form
from nwr_app.nwr_model import gamma_pdf
from scipy.special import gamma


def index(request):
    if request.method == 'POST':
        #form = temp_input_form(request.POST)
	form = pdf_input_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)
    else:
        #form = temp_input_form()
	form = pdf_input_form()

    return render(request, 'nwr_app/index.html', {'form': form})

def present_output(form):
    #cel_input = form.cel_input
    #s = convert_temp(cel_input)
    x_input = form.x
    theta_input = form.theta
    k_input = form.k
    s = gamma_pdf(x_input, theta_input, k_input)
    #return HttpResponse('Degree conversion function: Fahrenheit(%s C) = %s F' % (cel_input, s))
    return HttpResponse('Gamma(x, theta, k) for Gamma(%s) = %s' % (x_input, theta_input, k_input, s))