from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class LoginTestCase(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.client = Client()

    def test_login_and_logout(self):
        # ログインページにリダイレクトされる
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 302)
        # ログイン
        login_result = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login_result)
        # ログイン後のページにアクセス
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser のTODOリスト")
        # ログアウト
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ログアウトしました")


class SignupTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup(self):
        signup_data = {
            "username": "newuser",
            "password1": "userpassword1234",
            "password2": "userpassword1234",
        }
        response = self.client.post(reverse("signup"), data=signup_data)
        self.assertEqual(response.status_code, 302)
        # ログイン後のページにアクセス
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "newuser のTODOリスト")
        # データベースにユーザーが追加されている
        user_exists = User.objects.filter(username="newuser").exists()
        self.assertTrue(user_exists)
