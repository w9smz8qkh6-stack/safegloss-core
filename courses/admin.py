from django.contrib import admin

from .models import Course, CourseGlossary, CourseModeSchedule, Enrollment, Roster

admin.site.register([Course, CourseGlossary, CourseModeSchedule, Enrollment, Roster])
