# Create your tasks here

from celery import shared_task
from polls.models import SavedFunction
import matplotlib.pyplot as plt
from io import BytesIO
from .lambdaeval import evaluate
from time import time as posix


@shared_task
def plot_func ( funcid ) :
    o = SavedFunction.objects.get( id=funcid )
    try :
        days = o.interval * 60 * 60 * 24
        hours = o.dt * 60 * 60
        iposix = int ( posix () )
        ts = [ * range ( 1, iposix - ( iposix - days ), hours ) ]
        ys = [ evaluate ( o.textual, { 't' : t } ) for t in ts ]
        buf = BytesIO ()
        plt.plot ( ts, ys )
        plt.savefig ( buf, format='png' )
        buf.seek ( 0 )
        o.image = buf.read ()
        o.save ()
        buf.close ()
        # print ( 'success on plot_func', ts )
    except Exception as e :
        o.exception = str ( e )
        o.save ()
        # print ( 'catched failure on plot_func', e )
    return 0
