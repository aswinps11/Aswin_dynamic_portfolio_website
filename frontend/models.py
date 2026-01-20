from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    overview = models.TextField()
    highlights = models.JSONField(default=list)  # List of strings
    technical_implementation = models.TextField()
    quote = models.TextField()
    author_name = models.CharField(max_length=100)
    author_role = models.CharField(max_length=100)
    date = models.DateField()
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    technologies = models.CharField(max_length=200)
    live_url = models.URLField(blank=True)
    tags = models.JSONField(default=list)  # List of strings
    # Add image fields if needed

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    description = models.TextField()
    headline = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    delivery_time = models.CharField(max_length=50)
    revisions = models.CharField(max_length=50)
    support = models.CharField(max_length=50)
    badge = models.CharField(max_length=50, default='Premium Service')
    tech_stack = models.JSONField(default=list)  # List of strings
    testimonial = models.TextField()
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    tech_categories = models.JSONField(default=list)  # List of dicts with name and technologies

    def __str__(self):
        return self.title
