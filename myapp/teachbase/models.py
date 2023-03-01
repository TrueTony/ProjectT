from django.db import models


class Author(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role_id = models.PositiveIntegerField()
    auth_type = models.PositiveIntegerField()
    last_activity_at = models.PositiveIntegerField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Type(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner_id = models.PositiveIntegerField()
    thumb_url = models.URLField()
    cover_url = models.URLField()
    description = models.TextField()
    last_activity = models.DateTimeField()
    total_score = models.PositiveIntegerField()
    total_tasks = models.PositiveIntegerField()
    unchangeable = models.BooleanField()
    include_weekly_report = models.BooleanField()
    content_type = models.PositiveIntegerField()
    is_netology = models.BooleanField()
    bg_url = models.URLField()
    video_url = models.URLField()
    demo = models.BooleanField()
    custom_author_names = models.CharField(max_length=255)
    custom_contents_link = models.URLField()
    hide_viewer_navigation = models.BooleanField()
    duration = models.PositiveIntegerField()
    authors = models.ManyToManyField(Author)
    types = models.ManyToManyField(Type)

    def __str__(self):
        return self.name


class CourseDetails(Course):
    pass
