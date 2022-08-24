#I have created this file -- Sumayya
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     #return HttpResponse(request)
     return render(request,'index.html')
def analyze(request):
    #get the text
    djtext=request.POST.get('text','no text entered')
    #check the checkbox's values
    removepunc = request.POST.get('removepunc', 'off')
    capall = request.POST.get('capall', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #check which check box is on or checked
    if removepunc == "on":
        #analyzed = djtext
        punc_list= '''!()-[]{};:'"\,<>./?@#$%^&*_'''
        analyzed=""
        for char in djtext:
            if char not in punc_list:
                analyzed = analyzed+char
        params = {'purpose':'Remove Punctuation','analyzed_text':analyzed}
        djtext = analyzed   #overriding djtext
        #analyze the text
        #return HttpResponse("remove punctuation")
        #return render(request,'analyze.html',params)  #don't return here instead check for other condition(doing this for getting functionality of more than one checkboxes)
    if capall == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Convert into upper case','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed +char
        params = {'purpose':'Remove New Line','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    if spaceremover == "on":
        analyzed = ""
        for index , char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed+char
        params = {'purpose':'Remove Space','analyzed_text':analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = ""
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose':'Count the Characters','analyzed_text':analyzed}
        djtext = analyzed
    if (removepunc != "on" and capall != "on" and newlineremover != "on" and spaceremover != "on" and charcount != "on"):
        return HttpResponse("please select any operation")
    return render(request,'analyze.html',params)
