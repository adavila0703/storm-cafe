from django.test import TestCase
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from storm_inv.models import Snack, Person


class ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Snack.objects.create(name='snack1', amount=4, price=10)
        Snack.objects.create(name='snack2', amount=4, price=100)
        Person.objects.create(name='Person1', lname='Person1', money=100, movement='')
        Person.objects.create(name='Person2', lname='Person2', money=1000, movement='')


    def test_home(self):
        url = reverse('home')
        get_response = self.client.get(url)
        self.assertEqual(type(get_response), HttpResponse)
        self.assertEqual(get_response.status_code, 200)

    def test_add_person(self):
        url = reverse('add_person')
        get_response = self.client.get(url)
        post_response = self.client.post(url)
        self.assertEqual(type(get_response), HttpResponse)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(type(post_response), HttpResponse)
        self.assertEqual(post_response.status_code, 200)

    def test_person_home(self):
        url = reverse('person_home', args=[1])
        get_response = self.client.get(url)
        post_response = self.client.post(url)
        self.assertEqual(type(get_response), HttpResponse)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(type(post_response), HttpResponse)
        self.assertEqual(post_response.status_code, 200)

    def test_person_list(self):
        url = reverse('person_list')
        get_response = self.client.get(url)
        self.assertEqual(type(get_response), HttpResponse)
        self.assertEqual(get_response.status_code, 200)

    def test_edit_person(self):
        url = reverse('edit_person', args=[1])
        get_response = self.client.get(url)
        post_response = self.client.post(url)
        self.assertEqual(type(get_response), HttpResponse)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(type(post_response), HttpResponse)
        self.assertEqual(post_response.status_code, 200)

    def test_delete_person(self):
        url = reverse('delete_person', args=[1])
        get_response = self.client.get(url)
        post_response = self.client.post(url)
        self.assertEqual(type(get_response), None)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(type(post_response), HttpResponse)
        self.assertEqual(post_response.status_code, 200)

    def test_inventory_home(self):
        url = reverse('inventory_home')
        get_response = self.client.get(url)
        self.assertEqual(type(get_response), HttpResponse)
        self.assertEqual(get_response.status_code, 200)

    def test_inventory_list(self):
        url = reverse('inventory_list')
        get_response = self.client.get(url)
        self.assertEqual(type(get_response), HttpResponse)
        self.assertEqual(get_response.status_code, 200)

    def test_subtract_inventory(self):
        url = reverse('subtract_inventory', args=[1, 1])
        post_response = self.client.post(url)
        self.assertEqual(type(post_response), HttpResponseRedirect)
        self.assertEqual(post_response.status_code, 302)

    def test_add_inventory(self):
        url = reverse('delete_person')
        get_response = self.client.get(url)
        post_response = self.client.post(url)
        self.assertEqual(type(get_response), HttpResponse)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(type(post_response), HttpResponse)
        self.assertEqual(post_response.status_code, 200)

    def test_delete_inventory(self):
        url = reverse('delete_inventory', args=[2])
        post_response = self.client.post(url)
        self.assertEqual(type(post_response), HttpResponseRedirect)
        self.assertEqual(post_response.status_code, 302)

    def test_edit_inventory(self):
        url = reverse('edit_inventory', args=[1])
        get_response = self.client.get(url)
        post_response = self.client.post(url)
        self.assertEqual(type(get_response), HttpResponse)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(type(post_response), HttpResponse)
        self.assertEqual(post_response.status_code, 200)

    def test_loginuser(self):
        url = reverse('loginuser')
        get_response = self.client.get(url)
        post_response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(type(get_response), HttpResponse)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(type(post_response), HttpResponse)
        self.assertEqual(post_response.status_code, 200)

    def test_logoutuser(self):
        url = reverse('logoutuser')
        post_response = self.client.post(url)
        self.assertEqual(type(post_response), HttpResponseRedirect)
        self.assertEqual(post_response.status_code, 302)
