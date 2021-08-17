# Create your tasks here

from celery import shared_task


@shared_task
def count_functions () :
    from polls.models import SavedFunction
    return SavedFunction.objects.count ()
