# Create your tasks here

from celery import shared_task
from polls.models import SavedFunction
import matplotlib.pyplot as plt


@shared_task
def celery_test () :
    print ( '    !! celery test !! ' )
    count = SavedFunction.objects.count ()
    return count


@shared_task
def plot_func ( funcid ) :
    o = SavedFunction.objects.get( id=funcid )
    try :
        import matplotlib.pyplot as plt
        import io
        buf = io.BytesIO ()
        plt.plot ( [ *range(10) ], [ *range(10) ][::-1] )
        plt.savefig ( buf, format='png' )
        buf.seek ( 0 )
        o.image = buf.read ()
        o.save ()
        buf.close ()
        print ( 'success on plot_func' )
    except Exception as e :
        o.exception = str ( e )
        o.save ()
        print ( 'catched failure on plot_func', e )
    return 0
