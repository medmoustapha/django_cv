from django.contrib import admin
from .models import Person, Experience, Education, Skill,Langue,Formation

# Register your models here.
admin.site.register(Person)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Langue)
admin.site.register(Formation)
