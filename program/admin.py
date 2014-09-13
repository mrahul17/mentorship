from django.contrib import admin
from program.models import coordinators,alumni,students,departments,interest,studentpreferences,alumnipreferences

admin.site.register(alumni)
admin.site.register(students)
admin.site.register(departments)
admin.site.register(interest)
admin.site.register(studentpreferences)
admin.site.register(alumnipreferences)
admin.site.register(coordinators)
# Register your models here.
