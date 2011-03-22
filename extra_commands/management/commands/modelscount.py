from django.core.management.base import AppCommand
from django.core.management.base import BaseCommand
from optparse import make_option

class Command( BaseCommand ):
    option_list = BaseCommand.option_list
    help = 'Prints installed apps and models count for them.'

    requires_model_validation = True

    def handle(self, *args, **options):
        from django.db.models import get_models
        from django.db.models import get_apps

        lines = []
        
        apps = get_apps()
        for app in apps:
            lines.append( "    %s" % app.__name__ )
            for model in get_models( app ):
                lines.append( "\t[%s]" % model.__name__ + (" - %s objects" % model._default_manager.count()) )

        return "\n".join( lines ) + "\n"
