from django.shortcuts import render
from .forms import ImageForm, DocumentForm
from .models import Image
from django.http import HttpResponse
import io
from django import forms
def OnlyCAL(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            output = io.BytesIO()
            newdoc = request.FILES['docfile']
                #pandas calculations

            response = HttpResponse(
                output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=%s' % newdoc
            return response
    else:
        form = DocumentForm()
    return render(request, 'myapp/cal.html', { 'form': form})