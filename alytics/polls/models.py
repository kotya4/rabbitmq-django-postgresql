from django.db import models



class SavedFunction ( models.Model ) :
    # "id" serial NOT NULL PRIMARY KEY is immanent
    textual = models.CharField ( max_length=200 )
    image = models.FileField ( null=True )
    exception = models.TextField ( null=True )
    datetime = models.DateTimeField ( auto_now=True )
