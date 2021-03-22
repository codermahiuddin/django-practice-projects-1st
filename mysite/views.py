from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')


def userData(request):
    # Get user text and checkbox
    getData = request.POST.get('usertext','default')

    removepunc = request.POST.get('removepunc','off')
    uppercaseText = request.POST.get('uppercaseText','off')
    lowercaseText = request.POST.get('lowercaseText','off')
    extraLine = request.POST.get('extraLine','off')
    wordCount = request.POST.get('wordCount','off')


    # Remove Punctions
    if removepunc == 'on':
        analyzed = ""
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in getData:
            if i not in punc:
                analyzed = analyzed+i
        parems = {'purpose':'Remove Punctions', 'textData':analyzed}
        getData = analyzed
        
    #Convert text to Uppercase
    if uppercaseText == 'on':
        analyzed = ""
        analyzed = getData.upper()
        parems = {'purpose':'Uppercase', 'textData': analyzed}
        getData = analyzed

    
    #Convert text to Lowercase
    if lowercaseText == 'on':
        analyzed = ""
        analyzed = getData.lower()
        parems = {'purpose':'Lowercase', 'textData':analyzed }
        getData = analyzed

    #Count the number of Words
    if wordCount == 'on':
        analyzed = ""
        analyzed = len(getData.split())

        parems = {'purpose':"Count the number of Words in '" + getData + "'" , 'textData':analyzed}
        getData = analyzed

    
    #Remove extraLine
    if extraLine == 'on':
        analyzed = ""
        for i in getData:
            if i != '\n' and i != '\r':
                analyzed = analyzed+i
        parems = {'purpose':'Remove New Line', 'textData':analyzed}
        getData = analyzed


    if wordCount == 'off' and extraLine == 'off' and lowercaseText == 'off' and uppercaseText == 'off' and removepunc == 'off':
        return render(request,'error.html')
        
    return render(request,'userData.html',parems)