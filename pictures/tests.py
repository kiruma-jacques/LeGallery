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
        sectiond = Section.get_all_sections()
        self.assertTrue(len(sectiond) == 1)
