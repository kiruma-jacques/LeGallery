from django.test import TestCase
from .models import Upload, pin, Section
# Create your tests here.

class PinTestClass(TestCase):
    def setUp(self):
        self.newpin=pin(pin_name = 'states')

        self.newpin.save_pin()

    def test_pin_instance(self):
        self.assertTrue(isinstance(self.newpin, pin))

    def test_filter_pin(self):
        pins=pin.filter_by_pin()
        self.assertTrue(len(pins) > 0)

class SectionTestClass(TestCase):
    def setUp(self):
        self.newsection = Section(section_name = 'Tech')

        self.newsection.save_section()

    def test_section_instance(self):
        self.assertTrue(isinstance(self.newsection, Section))

    def test_get_all_section(self):
        sectiond= Section.get_all_sections()
        self.assertTrue(len(sectiond) == 1)

class UploadTestClass(TestCase):
    def setUp(self):
        self.newpin=pin(pin_name = 'states')
        self.newpin.save_pin()
        self.newsection = Section(section_name = 'Tech')
        self.newsection.save_section()
        self.newupload = Upload (title='test', name='nameth', description='testing model', location=self.newpin, category=self.newsection)
        self.newupload.save_upload()

    def test_upload_instance(self):
        self.assertTrue(self.newupload, Upload)

    def test_upload_save(self):
        self.newpintest=pin(pin_name = 'states 1')
        self.newpintest.save_pin()
        self.newsectiontest = Section(section_name = 'Tech 1')
        self.newsectiontest.save_section()
        self.newtest = Upload (title='test1', name='nameth1', description='testing model 1', location=self.newpintest, category=self.newsectiontest)
        self.newtest.save_upload()
        uploads = Upload.get_all_upload()
        self.assertTrue(len(uploads) == 2 )
