"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import UploadFileForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    form = UploadFileForm()
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,{'form':form})
    )

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
 
            return render(request, 'app/result.html')
    else:
        form = UploadFileForm()
    return render(request, 'app/index.html',{'form':form})


