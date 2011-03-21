from tddspry import NoseTestCase
from django.template import Template, Context

from cc42.settings import MEDIA_URL


class TestDjangoSettingsContextProcessor(NoseTestCase):
    def test_it(self):
        dummy_template = Template('MEDIA_URL:{{settings.MEDIA_URL}}')
        res = dummy_template.render()
        self.find_in(MEDIA_URL, res)
        
