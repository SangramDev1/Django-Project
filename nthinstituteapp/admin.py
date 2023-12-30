from django.contrib import admin
from .models import CoursesData

class AdminCourseData(admin.ModelAdmin):
    list_display=['course_name','duration','fee','start_date','timings','trainer_name','trainer_exp','training_mode']

admin.site.register(CoursesData,AdminCourseData)    


