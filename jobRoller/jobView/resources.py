#resources.py
#import tablib
from import_export import resources

from .models import CourseDescription, CourseKeyWords

class CourseDescriptionResource(resources.ModelResource):
	class Meta:
		model = CourseDescription
		imported_data = dataset.load(inventory.read().decode('utf-8'),format='csv')
		import_id_fields = ('course_id')

class CourseKeyWordsResource(resources.ModelResource):
		model = CourseKeyWords
		dataset = tablib.Dataset()
		imported_data = dataset.load(inventory.read().decode('utf-8'),format='csv')
		import_id_fields = ('course_id')