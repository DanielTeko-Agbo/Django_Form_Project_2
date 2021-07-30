from django.shortcuts import render,HttpResponseRedirect

from .forms import FormModelForm
from .models import Form

def formView(request):
    form = FormModelForm(request.POST)
    if request.method == 'POST':
        form = FormModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Form.objects.create(**form.cleaned_data)
            form = FormModelForm()
            return HttpResponseRedirect('../thanks/')
        else:
            form = FormModelForm()
    return render(request, 'base.html', {'form':form})

def thanksView(request):
    return render(request, 'thanks.html')
