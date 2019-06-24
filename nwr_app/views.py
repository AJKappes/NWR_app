from django.shortcuts import render
from django.http import HttpResponse
#from nwr_app.models import temp_input_form
#from nwr_app.nwr_model import convert_temp
from nwr_app.models import phos_input_form
from nwr_app.nwr_model import phos_func

def index(request):
    if request.method == 'POST':
        #form = temp_input_form(request.POST)
        form = phos_input_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)
    else:
        #form = temp_input_form()
        form = phos_input_form()

    return render(request, 'nwr_app/index.html', {'form': form})

def present_output(form):
    #cel_input = form.cel_input
    #s = convert_temp(cel_input)
    #x = form.x
    #theta = form.theta
    #k = form.k
    #s = gamma_pdf(x, theta, k)
    blood = form.blood
    fish_by = form.fish_by
    paper_pulp = form.paper_pulp
    ob = form.ob
    gt = form.gt
    manure = form.manure
    s = phos_func(blood, fish_by, paper_pulp, ob, gt, manure)
    #return HttpResponse('Degree conversion function: Fahrenheit(%s C) = %s F' % (cel_input, s))
    #return HttpResponse('Gamma%s = %s' % ((x, theta, k), s))
    response = HttpResponse()
    response.write('<head><script src=\'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML\' async></script></head>')
    response.write('For input values [blood, fish byproduct, paper pulp, OB, GT, manure)] = [{}, {}, {}, {}, {}, {}], phosphorus (kg) = {}'.format(blood, fish_by, paper_pulp, ob, gt, manure, s))
    return response
