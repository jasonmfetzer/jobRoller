from .models import Keyword,Course,CourseDescription, CourseKeyWords
import django_filters




class CourseFilter(django_filters.FilterSet):
	course_name = django_filters.CharFilter(lookup_expr='icontains')
	course_description = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Course
		fields = '__all__'



class KeywordFilter(django_filters.FilterSet):
	keyword = django_filters.CharFilter(lookup_expr='icontains')
	#keywords = django_filters.CharFilter(course_pneumonic__in=Course.objects.filter(course_id = course_id))
	class Meta:
		model = Keyword
		fields = ['keyword']
