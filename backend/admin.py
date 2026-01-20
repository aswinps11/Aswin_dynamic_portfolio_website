from django.contrib import admin
from .models import HomeContent, Skill, Education, Experience,User

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class HomeContentAdmin(admin.ModelAdmin):
    inlines = [SkillInline, EducationInline, ExperienceInline]

# Register your models here.
admin.site.register(HomeContent, HomeContentAdmin)
admin.site.register(User)