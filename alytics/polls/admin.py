from django.contrib import admin

from .models import SavedFunction


class SavedFunctionAdmin ( admin.ModelAdmin ) :
    fields = [ 'textual', 'dt', 'interval' ]
    list_display = [ 'custom_display', 'custom_display2' ]

    @admin.display ( description='custom_display' )
    def custom_display ( self, instance ) :
        return 0

    @admin.display ( description='custom_display2' )
    def custom_display2 ( self, instance ) :
        return 1

admin.site.register ( SavedFunction, SavedFunctionAdmin )

# admin.site.register ( SavedFunction )



""" view must contain

{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li  {% if message.tags %} class=" {{ message.tags }} " {% endif %}> {{ message }} </li>
    {% endfor %}
</ul>
{% endif %}

"""
