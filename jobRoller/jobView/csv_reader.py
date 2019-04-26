import django
from django.conf import settings

settings.configure()
django.setup()

import csv
from models import CourseKeyWords, CourseDescription

with open('keywords.csv', encoding='utf-8', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p=CourseKeyWords(
        # The header row values become your keys
        course_id = row['course_id'],
        keyword = row['keyword']
        )
        p.save()
        # etc....

        # new_revo = Revo(SuiteName=suite_name, TestCase=test_case,...)
        # new_revo.save()

#/Users/jasonfetzer/Desktop/iit_final_project/jobRoller/jobRoller