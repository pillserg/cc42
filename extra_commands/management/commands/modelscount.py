from django.core.management.base import AppCommand
from django.core.management.base import BaseCommand
import sys


class Command( BaseCommand ):
    help = 'Prints installed apps and models count for them.'

    requires_model_validation = True

    def handle(self, *args, **options):
        from django.db.models import get_models
        from django.db.models import get_apps

        lines = []
        
        apps = get_apps()
        for app in apps:
            lines.append( '    %s' % app.__name__ )
            for model in get_models( app ):
                lines.append( '\t[%s]' % model.__name__ +
                             (' - %s objects' % model._default_manager.count()) )
                
        sys.stderr.write(  ''.join(( 'error: ','\n'.join(lines), '\n' ))  )
        return '\n'.join( lines ) + '\n'
