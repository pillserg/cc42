from django.conf import settings
from django.core.urlresolvers import reverse

from tddspry.django import HttpTestCase, DatabaseTestCase
from tddspry import NoseTestCase

from cc42.contacts.models import UserDetail


test_data = {
    'name': 'Serg',
    'last_name': 'Piljavsky',
    'email': 'pill@i.ua',
    'jabber': 'pillserg@jabber.ru',
    'skype': 'pillserg',
    'other_contacts': 'pill.sv0@gmail.com\
                      ICQ:289861503',
    'bio': 'Born in Kiev (1987) \
           Graduated from NAU (2010)\
           Currently looking for work.',
    'date_of_birth': '1987-09-03',
    }


class TestContactsUserDetailModel(DatabaseTestCase):

    new_name = 'Jane'

    def make_test_obj(self):
        kw_str = ', '.join(['='.join((str(k), ("'''" + str(v) + "'''")))
                            for k, v in test_data.items()])
        run_str = 'self.assert_create(UserDetail, %s)' % kw_str
        eval(run_str)

    def test_create(self):
        self.make_test_obj()

    def test_read(self):
        self.make_test_obj()
        self.assert_read(UserDetail, name=test_data['name'])

    def test_update(self):
        self.make_test_obj()
        self.assert_update(UserDetail, name=self.new_name)

    def test_delete(self):
        self.make_test_obj()
        UD = UserDetail.objects.get(name=test_data['name'])
        self.assert_delete(UD)


class Test_MainPageBio(HttpTestCase):

    def test_userDetailMustBeOnMainPage(self):
        """
           Next things must be present on main page:
           Name, Last name, Email: email, Jabber: JID,
           Skype: id, Other contacts: Multiline, Bio:, Multiline
           Date of birth"""
        if UserDetail.objects.count():
            details = UserDetail.objects.all()[0]
        self.go(reverse('show_main_page'))
        self.find(details.name)
        self.find(details.last_name)
        self.find(details.email)
        self.find(details.jabber)
        self.find(details.skype)
        self.find(details.other_contacts)
        self.find(details.bio, flat=True)
        self.find(str(details.date_of_birth))


class TestContactsForm(NoseTestCase):

    def test_aceppting_valid_data(self):
        from cc42.contacts.forms import UserDetailForm
        from cc42.contacts.models import UserDetail

        form = UserDetailForm(instance=UserDetail.objects.get(id=1))
        self.assert_false(form.is_bound)
        form = UserDetailForm(test_data, instance=UserDetail.objects.get(id=1))
        self.assert_true(form.is_bound)
        self.assert_true(form.is_valid())

    def test_not_accepting_invalid_data(self):
        pass


class TestContactFormPage(HttpTestCase):

    def test_edit_form_login_req(self):
        self.go(reverse('show_edit_contacts'))
        self.notfind('user_profile_edit')

    def test_edit_form_accepts_login(self):
        self.login('admin', 'admin')
        self.go(reverse('show_edit_contacts'))
        self.find('user_profile_edit')

    def test_form_fails_on_invalid_data(self):
        self.login('admin', 'admin')
        self.go(reverse('show_edit_contacts'))
        self.fv('1', 'email', 'Wrong_email')
        self.fv('1', 'name', '')
        self.submit()
        self.find('errorlist')

    def test_passes_on_valid_data(self):
        self.login('admin', 'admin')
        self.go(reverse('show_edit_contacts'))
        for k, v in test_data.items():
            self.fv('1', k, v)
        self.submit()
        self.notfind("error")


class TestContactForm(DatabaseTestCase):

    def test_save_form(self):
        from cc42.contacts.forms import UserDetailForm
        from cc42.contacts.models import UserDetail

        form = UserDetailForm(test_data, instance=UserDetail.objects.get(id=1))
        form.save()
        UD = UserDetail.objects.get(id=1)
        self.assert_equal(UD.name, test_data['name'])
