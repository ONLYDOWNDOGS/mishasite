from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

TECHNIQUE = (
    (0,"Charcoal"),
    (1,"Photoshop"),
    (2,"Painting"),
    (3,"Reel"),
    (4,"Sketching"),
    (5,"Illustrator")
)

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # To use if the images are already on the local machine, don't think it'll work for site owner
    # adding new files themselves
    # image = models.FilePathField(path="/img")
    drawing = models.ImageField(upload_to='images')
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title