from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def kirr_redirect_view(request, *args, **kwargs):  #function based view FBV
	return HttpResponse("hello")


class KirrCBView(View):  #class based view  CBV
	def get(self, request, *agrs, **kwargs):
		return HttpResponse("hello again")
	
		