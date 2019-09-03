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
    s = phos_func(blood, fish_by, paper_pulp, ob, gt, manure, loc=form.loc, soil_test=form.soil_test, acres=form.acres)
    response = HttpResponse()
    response.write('<head><script src=\'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML\' async></script></head>')
    response.write(
'<p>For input values {{blood, fish byproduct, paper pulp, OB, GT, manure, location, soil test, acres}} = {{{}, {}, {}, {}, {}, {}, {}, {}, {}}}:</p> <p></p> <p>Total AD phosphorus ouput is {} lbs.</p> <p></p> <p>Based on your soil test, your phosphorus index categorization is: <em>{}</em>.</p> <p></p> <p>Per your phosphorus index categorization, the recommended range of phosphorus application is {} lbs/acre.</p> <p>Phosphorus lbs/acre from AD output is {}.</p> <p></p> <p>Phosphorus application decision is: <em>{}</em>.</p> <p>Total revenue from AD inputs: ${}</p>'.format(blood, fish_by, paper_pulp, ob, gt, manure, form.loc, form.soil_test, form.acres, s[0], s[2], s[3], s[1], s[4], s[5]))
    return response
