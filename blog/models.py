from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    content_rendered = models.TextField(editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField()
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def clean(self):
        try:
            import markdown
            self.content_rendered = markdown.markdown(self.content)
        except ImportError:
            self.content_rendered = self.content

    class Meta:
        ordering = ['-updated_at']
