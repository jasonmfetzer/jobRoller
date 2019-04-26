from django.db import models

# Create your models here.





class CourseDescription(models.Model):
	course_pneumonic = models.CharField(max_length=5)
	course_id = models.IntegerField()
	required = models.BooleanField(default=False)
	course_description = models.TextField()
	#credits = models.IntegerField()

	def __str__(self):
		return '{},{},{}'.format(self.course_pneumonic, self.course_id, self.required)

class CourseKeyWords(models.Model):
	#need pneumonic
	course_id = models.IntegerField()
	keyword = models.TextField()

	def __str__(self):
		return '{},{}'.format(self.course_id, self.keyword)


class Course(models.Model):
	course_pneumonic = models.CharField(max_length=5)
	course_name = models.TextField()
	course_id = models.IntegerField()
	required = models.BooleanField(default=False)
	course_description = models.TextField()

	def __str__(self):
		return '{},{},{}'.format(self.course_pneumonic, self.course_id, self.course_name)

class Keyword(models.Model):
	course_pneumonic = models.CharField(max_length=5)
	course_id = models.IntegerField()
	keyword = models.TextField()

	def __str__(self):
		return '{},{}, {}'.format(self.course_id, self.course_pneumonic, self.keyword)		