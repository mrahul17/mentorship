from django.contrib import admin
from program.models import alumni,students,departments,interest,studentpreferences,alumnipreferences

admin.site.register(alumni)
admin.site.register(students)
admin.site.register(departments)
admin.site.register(interest)
admin.site.register(studentpreferences)
admin.site.register(alumnipreferences)

# Register your models here.
