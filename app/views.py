"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import UploadFileForm
from projectoxford.Client import Client
from projectoxford.Emotion import Emotion
from tempfile import TemporaryFile
from django.conf import settings
from PIL import ImageDraw
from PIL import Image
import base64

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
            modified, happyscore = handle_uploaded_file(file)
            modified.seek(0)
            image = base64.b64encode(modified.read())
 
            return render(request, 'app/result.html', {'image': image, 'ishappy':happyscore})
    else:
        form = UploadFileForm()
    return render(request, 'app/index.html',{'form':form})

def handle_uploaded_file(file):
    client = Client.emotion(settings.OXFORD_KEY)
    recognizeResult  = client.recognize({'stream': file})

    im = Image.open(file)
    draw = ImageDraw.Draw(im)
 
    happyscore = 0

    for emotionResult in recognizeResult:
        rect = emotionResult['faceRectangle']
        x = emotionResult['faceRectangle']['left']
        y = emotionResult['faceRectangle']['top']
        x1 = emotionResult['faceRectangle']['left'] + emotionResult['faceRectangle']['width']
        y1 = emotionResult['faceRectangle']['top'] + emotionResult['faceRectangle']['height']
 
        draw.rectangle([x,y,x1,y1])

        happiness = emotionResult['scores']["happiness"]
        sadness = emotionResult['scores']["sadness"]
 
        if (happiness > sadness):
            happyscore = happyscore + 1
        else:
            happyscore = happyscore - 1
        
    modified = TemporaryFile()
    im.save(modified,'JPEG')
    return modified, happyscore