from django.shortcuts import render, get_object_or_404, HttpResponse
import csv, io
from .filters import CourseFilter, KeywordFilter
from django.contrib import messages
#from django.contrib.auth.decorators import permission_required
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Keyword, Course,CourseDescription, CourseKeyWords

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen 
import pprint
import re
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import URLForm

def get_name(request):
	list1='No Relevant Technologies Found.'
	#form_class = URLForm
	#form = form_class(request.POST or None)
	if request.method == 'POST':
		form = URLForm(request.POST)
		text = request.POST.get('text')

		if form.is_valid():

			print('I am valid')
			hdr = {'User-Agent': 'Mozilla/5.0'}
			#req = Request(site,headers=hdr)
			req = Request(text, headers=hdr)
			list1=[]
			page = urlopen(req)
			soup=BeautifulSoup(page,'lxml')
			for items in soup.find_all('item'):
				list1.append(items.title.get_text())
				context={
				"list1":list1
				}
			#list1=URLForm.cleaned_data
			#return list1
			
			return HttpResponseRedirect('/soup/')
	else:
		form = URLForm()
	return render(request, 'soup.html', {'list1': list1})
	#return render(request, 'soup.html', {'form': form})


def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def index(request):
	return render(request, 'index.html')
def about(request):
	return render(request, 'about.html')
def futures(request):
	return render(request, 'futures.html')


#@permission_required('admin.can_add_log_entry')


def course_detail_view(request, id=None):
	course = get_object_or_404(Course, id=id)
	context = {'course':course,}
	return render(request, 'course_detail.html', context)


def kw_detail_view(request, id=None):
	keyword=get_object_or_404(Keyword, id=id)
	slug_url_kwarg = 'course_id'
	context = {'keyword':keyword,}
	return render(request, 'kw_detail.html', context)

def search(request):
	course = Course.objects.all()
	course_filter = CourseFilter(request.GET, queryset=course)
	return render(request, 'search.html', {'filter': course_filter})

def kw_search(request):
	keyword = Keyword.objects.all()
	keyword_filter = KeywordFilter(request.GET, queryset=keyword)
	return render(request, 'kw_search.html', {'filter':keyword_filter})


def request_page(request):
	if request.GET.get('mybtn'):
		pass
	else:
		pass


def rssfeed(request):
	#form = URLForm['url']
	site=input("Enter a URL: ") #https://rss.sciencedaily.com/computers_math/computer_programming.xml"
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = Request(site,headers=hdr)
	#req = Request(form, headers=hdr)
	list1=[]
	page = urlopen(req)
	soup=BeautifulSoup(page,'lxml')
	for items in soup.find_all('item'):
		list1.append(items.title.get_text())
	context={
		"list1":list1
		}
	return render(request,'soup.html',context)





def soupify(request):
	context = {}
	if request.method == 'POST':
		site = request.POST.get('city')
		hdr = {'User-Agent': 'Mozilla/5.0'}
		
		req = Request(site,headers=hdr)
		page = urlopen(req)
		soup = BeautifulSoup(page, "lxml")
		links = soup.findAll("li")
		links2 = soup.findAll(string='icon-engineering')
		links3 = soup.findAll('<li class=')
		pattern = re.compile('icon-engineering')
		attributes_dictionary = soup.find('li').attrs	

		li =[]

		for ultag in soup.findAll('ul', {'class': 'accordion-tabs'}):
			for litag in ultag.findAll('li'):
				li.append(clean_word(litag.text))
			#print(litag.text)
		context['temp'] = li
		#for i in li:
		#	print(clean_word(i))
	return render(request, 'soupify.html', context)


def clean_word(word):
	word=word.replace("Languages", '')
	word=word.replace("Frameworks", '')
	word=word.replace("Libraries", '')
	word=word.replace("Databases", '')
	word=word.replace("Analytics", ' Analytics')
	word=word.replace("Design", ' Design')
	word=word.replace("Management", ' Management')
	word=word.replace("CRM", ' CRM')
	word=word.replace("Email", ' Email')
	return word


class KeywordListView(ListView):
	template_name = 'kw_list.html'
	model = CourseKeyWords
	queryset = CourseKeyWords.objects.filter(keyword='.NET')
	#context_object_name = 'kw'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		#context['now'] = timezone.now()
		return context

	# def get_queryset(self):
	# 	return CourseKeyWords.objects.filter(required=True)

