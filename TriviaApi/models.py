from django.db import models

# Create your models here.
from django.db import models


# declare a new model with a name "GeeksModel"
class TriviaModel(models.Model):
    # fields of the model
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    test_at = models.DateTimeField(auto_now_add=True)
    player_name=models.CharField(max_length=50)
    flag_color=models.CharField(max_length=100)
    def __str__(self):
        return self.id