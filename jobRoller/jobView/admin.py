from django.contrib import admin
from .models import Keyword, Course,CourseDescription, CourseKeyWords
from import_export.admin import ImportExportModelAdmin

# Register your models here.



@admin.register(CourseDescription)
class CourseDescriptionAdmin(ImportExportModelAdmin):
	pass
#admin.site.register(CourseDescription)

@admin.register(CourseKeyWords)
class CourseKeyWordsAdmin(ImportExportModelAdmin):
	pass

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
	pass

@admin.register(Keyword)
class KeywordAdmin(ImportExportModelAdmin):
	pass