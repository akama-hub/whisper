from django.http import HttpResponseRedirect
from django.shortcuts import render

from minutes_app.whisper import WhisperModelWrapper
from .forms import UploadFileForm
from django.http import HttpResponse

import sys
import csv
from datetime import datetime
# from faster_whisper import main

def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            sys.stderr.write("*** file_upload *** aaa ***\n")
            extract_audio(request.FILES['file'])
            file_obj = request.FILES['file']
            sys.stderr.write(file_obj.name + "\n")
            return HttpResponseRedirect('/success/url')
    else:
        form = UploadFileForm()
    return render(request, 'minutes_app/index.html', {'form': form})

def extract_audio(movie):
    model = WhisperModelWrapper()
    segments = model.transcribe(audio=movie)
    for segment in segments:
        with open(f'documents/{datetime.now().strftime("%m%d_%H%M")}.csv', "a") as f:
            writer = csv.writer(f)
            writer.writerow([segment.text])



#recording 要
# def recording(request):
#     if request.method == "POST":
#         if "start_button" in request.POST:
#             main()

def success(request):
    str_out = "Success!<p />"
    str_out += "成功<p />"
    return HttpResponse(str_out)

def success_url(request):
    return render(request, 'minutes_app/success.html')
