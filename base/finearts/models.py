from django.db import models

# Field Choices
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

TECHNIQUE = (
    (0,"Charcoal"),
    (1,"Photoshop"),
    (2,"Painting"),
    (4,"Sketching"),
    (5,"Illustrator"),
    (6,"Pet_Portraits")
)

class Portfolio(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    drawing = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    artstyle = models.IntegerField(choices=TECHNIQUE, default=2)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.title}, {self.artstyle}'