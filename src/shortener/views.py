from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL

# Create your views here.
# def kirr_redirect_view(request, shortcode=None ,*args, **kwargs):  #function based view FBV
# 	obj = get_object_or_404(KirrURL, shortcode=shortcode)
# 	#do something
# 	return HttpResponseRedirect(obj.url)


def home_view_fbv(request, *args, **kwargs):
	if request.method == "POST":
		print(request.POST)
	return render(request, "shortener/home.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title": "Kirr.co",
			"form": the_form
		}
		return render(request, "shortener/home.html", context)  #Try Django 1.8  & 1.9 

	def post(self, request, *args, **kwargs):
		# some_dict = {}
		# some_dict['url']	#this will give error
		# some_dict.get('url', "http://google.com") #it will return None
		# print(request.POST)
		# print(request.POST.["url"])
		# print(request.POST.get("url"))
		form = SubmitUrlForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data.get("url"))

		context = {
			"title": "Kirr.co",
			"form": form
		}
		return render(request, "shortener/home.html", context)


class KirrCBView(View):  #class based view  CBV
	def get(self, request, shortcode=None ,*args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		return HttpResponseRedirect(obj.url)
	
	# def post(self, request, *args, **kwargs):
	# 	return HttpResponse()


