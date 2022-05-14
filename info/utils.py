from .models import *

menu = [{'title': 'Home Page', 'url_name': 'home'},
        {'title': 'Заполнение формы', 'url_name': 'index'}
        ]

class DataMixin:
    def get_guest_context(self, **kwargs):
        context = kwargs
        context[menu] = menu