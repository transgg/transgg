from django.db import models

class Page(models.Model):
    """Represents a non-category/question page on the site"""
    # Name of the page
    name = models.CharField(max_length=48)
    # Slug (url identifier) field
    slug = models.SlugField()
    # Contents of the page
    body = models.TextField()
    # Whether the page is visible in navigation
    visible = models.BooleanField(default=True)
    # (Optional) fontawesome icon class (e.g fa-rocket) for navigation
    icon = models.CharField(max_length=24, blank=True)
    # Whether this page should be the front-page
    index = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    """Represents a category that questions can belong to"""
    # Title of category
    title = models.CharField(max_length=32)
    # Slug (url identifier) field
    slug = models.SlugField()
    # (Optional) short description of category
    description = models.TextField(blank=True)
    # Whether category and its questions are visible
    visible = models.BooleanField(default=True)
    # (Optional) fontawesome icon class (e.g fa-rocket) for navigation
    icon = models.CharField(max_length=24, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Question(models.Model):
    """Represents a question with an answer on a specific topic"""
    # Question
    title = models.CharField(max_length=56)
    # Slug (url identifier) field
    slug = models.SlugField()
    # Basic answer
    answer = models.TextField()
    # (Optional) long-form answer for more in-depth questions
    long_answer = models.TextField(blank=True)
    # (Optional) source for the information
    source = models.TextField(blank=True)
    # Category question belongs to
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)
    # Date housekeeping - when created & last updated
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Link(models.Model):
    """Represents a link to an external resource"""
    # Name of the resource
    name = models.CharField(max_length=56)
    # Linkable URL of the resource
    url = models.CharField(max_length=256)
    # (Optional) short description of the resource
    description = models.TextField(blank=True)
    # (Optional) fontawesome icon class (e.g fa-rocket) for navigation
    icon = models.CharField(max_length=24, blank=True)

    def __str__(self):
        return self.name