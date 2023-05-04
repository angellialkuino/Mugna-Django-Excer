from django.test import TestCase, Client
from exercises.models import Book,Publisher,Author,Classification
from django.urls import reverse
from django.contrib.auth.models import User
from exercises.forms import AuthorForm

# Create your tests here.

class SearchTests(TestCase):
    def setUp(self):
        a1 = Author.objects.create(first_name="Aaaa", last_name="Jjjj", email="aaa@gmail.com")
        a2 = Author.objects.create(first_name="Bbb", last_name="Jjjj", email="aaa@gmail.com")

        p1 = Publisher.objects.create(name="JapABC", city="Tokyo", country="Japan", website="https://abc.com")
        p2 = Publisher.objects.create(name="penguin", city="Beijing", country="China", website="https://p.com")

    def test_search_author(self):
        query="a"
        response = self.client.get(reverse("search-author"), {"query":query})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["results"],
            [r for r in Author.objects.filter(first_name__icontains=query)]
        )
    
    def test_search_publisher(self):
        query="a"
        response = self.client.get(reverse("search-publisher"), {"query":query})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["results"],
            [r for r in Publisher.objects.filter(name__icontains=query)]
        )


class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="Jasonderulo", email="jd@gmail.com", password="jd")


    def test_successful_login(self):
        response = self.client.post(reverse("login"), {"username":"Jasonderulo", "password":"jd"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_failed_login(self):
        response = self.client.post(reverse("login"), {"username":"Jasonderulo", "password":"jj"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')


class LogoutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="Jasonderulo", email="jd@gmail.com", password="jd")
        self.client.force_login(self.user)

    def test_successful_logout(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))


class DetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="Jasonderulo", email="jd@gmail.com", password="jd")
        a1 = Author.objects.create(first_name="Aaaa", last_name="Jjjj", email="aaa@gmail.com")
        p1 = Publisher.objects.create(name="JapABC", city="Tokyo", country="Japan", website="https://abc.com")
        c1 = Classification.objects.create(code='001', name='name1', description='description1')
        b1 = Book.objects.create(title='Good Gasby', author=a1, classification=c1, publisher=p1)
        b2 = Book.objects.create(title='ANother Gasby', author=a1, classification=c1, publisher=p1)


    def test_anonymous_cannot_acces_page(self):
        response = self.client.get(reverse("book-details", args=[1]))
        self.assertRedirects(response, "/accounts/login/?next=/books/1")

    def test_authenticated_can_acces_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("book-details", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["book"], Book.objects.get(id=1))


class AddAuthorTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username="Jasonderulo", email="jd@gmail.com", password="jd")
        a1 = Author.objects.create(first_name="Aaaa", last_name="Jjjj", email="aaa@gmail.com")
    
    def test_anonymous_cannot_access_page(self):
        response = self.client.get(reverse("create-author"))
        self.assertRedirects(response, "/accounts/login/?next=/create-author/")

    def test_add_author(self):
        self.client.force_login(self.user)
        data = {
            "first_name": "Nacho",
            "last_name": "Cat",
            "email": "ncat@gmail.com"
        }
        response = self.client.post(reverse("create-author"), data=data)
        self.assertTemplateUsed(response, "crud_results.html")
        self.assertContains(response,"Nacho")
        self.assertContains(response,"Aaaa")
        self.assertEqual(Author.objects.count(), 2)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, "create_obj.html")

    def test_update_author(self):
        self.client.force_login(self.user)
        data = {
            "first_name": "Makko",
            "last_name": "Cat",
            "email": "ncat@gmail.com"
        }
        response = self.client.post(reverse("update-author", args=[1]), data=data)
        self.assertTemplateUsed(response, "crud_results.html")
        self.assertContains(response,"Makko")
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(response.status_code, 200)

    def test_delete_author(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("delete-author", args=[1]))
        self.assertTemplateUsed(response, "crud_results.html")
        self.assertNotContains(response,"Jasonderulo")
        self.assertEqual(Author.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
