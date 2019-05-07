from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('value','off')
    text=request.POST.get('text','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    space = request.POST.get('space','off')
    charcount = request.POST.get('charcount','off')

    if text=='on':
            analyzed=''
            punctuations='''!@#$%^&*()_+{}:"<>?,./;'[]=-'''
            for i in djtext:
                if i not in punctuations:
                    analyzed = analyzed+i
            params = {'purpose':'Removed punctuations','analyzed_text': analyzed}
            djtext=analyzed

    if fullcaps=='on':
        analyzed=''
        for i in djtext:
            analyzed=analyzed+i.upper()
        params = {'purpose': 'done changes', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremove=='on':
        analyzed=''
        for i in djtext:
            if i!='\n' and i!='\r':
                analyzed=analyzed+i
        params = {'purpose': 'newline removed', 'analyzed_text': analyzed}
        djtext=analyzed

    if space=='on':
        analyzed=''
        for i in djtext:
            if i!=' ':
                analyzed=analyzed+i
        params ={'purpose':'request is not done','analyzed_text':analyzed}
        djtext=analyzed

    if charcount=='on':
        count=0
        for i in djtext:
            if i!=' ':
                count=count+1
        params={'purpose':'dsckmsckm','analyzed_text':count}
        djtext=analyzed


    return render(request,'analyze.html',params)