from django.db import models


class Profile(models.Model):
    BG_CHOICES = (("blue", "Blue"), ("yellow", "Yellow"), ("green", "Green"))

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    profile_id = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="links"
    )

    def __str__(self):
        return f"{self.name} | {self.url}"
