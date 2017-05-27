from django.test import TestCase
from catalog.models import Author

"""
General scheme for tests
class YourTestClass(TestCase):

    @classmethod

    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
"""
#setUpTestData() is called once at the beginning of the test run for class-level setup.
#You'd use this to create objects that aren't going to be modified or changed in any of the test methods.

#setUp() is called before every test function to set up any objects that may be
# modified by the test (every test function will get a "fresh" version of these objects).

#Django specific asserions: https://docs.djangoproject.com/en/1.10/topics/testing/tools/#assertions
# Python assertions: https://docs.python.org/3/library/unittest.html#assert-methods


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name="Karol", last_name="Fiutek")

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label=author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'Imię')

    def test_author_name_str(self):
        author=Author.objects.get(id=1)
        return '%s, %s'%(author.last_name, author.first_name)
        return self. assertEquals(expected_name,author.str())


    def test_author_get_absolute_url(self):
        author=Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/catalog/autor/1')
