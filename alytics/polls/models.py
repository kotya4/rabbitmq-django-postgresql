from django.db import models



class SavedFunction ( models.Model ) :
    # "id" serial NOT NULL PRIMARY KEY is immanent
    textual = models.CharField ( max_length=100 )
    dt = models.IntegerField ( default=-1 )
    interval = models.IntegerField ( default=-1 )
    image = models.FileField ( blank=True, null=True )
    exception = models.TextField ( blank=True, null=True )
    datetime = models.DateTimeField ( auto_now=True )
