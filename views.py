from django.http import HttpResponse


def index(request):
 someproperties = request.path
 return HttpResponse(someproperties)


def products(request):
 return HttpResponse('ABOUT products of OUR COMPANY...')


def gallery(request):
 return HttpResponse('gallery ...')


def jobs(request):
 return HttpResponse('jobs in OUR COMPANY...')


def about(request):
 return HttpResponse('ABOUT OUR COMPANY...')
