from django.shortcuts import render
from django.http import HttpResponse
from .forms import WingForm
from django.template import loader
from django.core.paginator import Paginator
from .models import Wing
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect

def add_wing(request):
    if request.method == 'POST':
        form = WingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Ala criada com sucesso! <a href="/wings/">Voltar</a>')
    else:
        form = WingForm()
    return render(request, 'add_wing.html' , {'form': form})

def wings(request):
    wings = Wing.objects.all().values().order_by('code')
    template = loader.get_template('wings.html')
    paginator = Paginator(wings, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'wings': page_obj,
    }
    
    return HttpResponse(template.render(context, request))

def delete(request, code):
    patient = Wing.objects.get(code=code)
    patient.delete()
    return HttpResponseRedirect('/wings/')

def update(request, code):
    wing = get_object_or_404(Wing, code=code)
    if request.method == 'POST':
        form = WingForm(request.POST, instance=wing)
        if form.is_valid():
            form.save()
            return redirect('wings')  # Redireciona para a lista de alas
    else:
        form = WingForm(instance=wing)
    return render(request, 'add_wing.html', {'form': form})