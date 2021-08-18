from django.db import models
import base64
import json


class SavedFunction ( models.Model ) :
    # "id" serial NOT NULL PRIMARY KEY is immanent
    textual = models.CharField ( max_length=100 )
    dt = models.IntegerField ( default=-1 )
    interval = models.IntegerField ( default=-1 )
    image = models.BinaryField ( blank=True, null=True )
    exception = models.TextField ( blank=True, null=True )
    datetime = models.DateTimeField ( auto_now=True )

    def __str__ ( self ) :
        id = self.id
        textual = self.textual
        dt = self.dt
        interval = self.interval
        image = type ( self.image )
        exception = self.exception
        datetime = self.datetime
        return f'{ id } { textual } { dt } { interval } { image } { exception } { datetime }'

    def dictify ( self ) :
        r = {
            'id': str ( self.id ),
            'textual': str ( self.textual ),
            'dt': str ( self.dt ),
            'interval': str ( self.interval ),
            'image': base64.b64encode ( self.image ) .decode ( 'utf-8' ) if self.image else None,
            'exception': str ( self.exception ) if self.exception else None,
            'datetime': str ( self.datetime ),
        }
        return r

