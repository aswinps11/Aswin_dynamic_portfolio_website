from django.db import models

# Create your models here.
class HomeContent(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    
    # About Me section fields
    about_title = models.CharField(max_length=200, default="About Me")
    about_paragraph1 = models.TextField(default="Short paragraph describing who you are, your degree, and what you are looking for.")
    about_paragraph2 = models.TextField(default="Another short paragraph about your interests, learning mindset, and goals.")
    experience = models.CharField(max_length=100, default="Fresher / Internship Experience")
    degree = models.CharField(max_length=100, default="B.Tech in Information Technology")
    location = models.CharField(max_length=100, default="Kozhikode, Kerala, India")
    email = models.EmailField(default="yourmail@example.com")
    phone = models.CharField(max_length=20, default="+91 XXXXXXXXXX")
    availability = models.CharField(max_length=50, default="Open to Work")
    
    # Resume file
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, help_text="Upload your resume PDF")

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    home_content = models.ForeignKey(HomeContent, on_delete=models.CASCADE, related_name='skills')
    
    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year_range = models.CharField(max_length=50)
    degree_level = models.CharField(max_length=100)
    home_content = models.ForeignKey(HomeContent, on_delete=models.CASCADE, related_name='educations')
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Experience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    home_content = models.ForeignKey(HomeContent, on_delete=models.CASCADE, related_name='experiences')
    
    def __str__(self):
        return f"{self.position} at {self.company}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, blank=True, help_text="Technologies used in this project")
    file = models.FileField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)  # optional if you want phone
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


# User
class User(models.Model):
    name=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    