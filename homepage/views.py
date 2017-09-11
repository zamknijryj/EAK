from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage/homepage.html')


def abc(request):
    return render(request, 'homepage/abc.html')


def rejestr_zolnierzy(request):
    return render(request, 'homepage/rejestr.html')


def rekrutacja(request):
    return render(request, 'homepage/rekrutacja.html')


def majordom_koronny(request):
    return render(request, 'homepage/majordom_koronny.html')


def obrona_terytorialna(request):
    return render(request, 'homepage/obrona_terytorialna.html')


def zakon(request):
    return render(request, 'homepage/zakon.html')


def sily_operacyjne(request):
    return render(request, 'homepage/sily_operacyjne.html')


def gwardia(request):
    return render(request, 'homepage/gwardia.html')
