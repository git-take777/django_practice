# from django.test import TestCase→コメントアウト(書籍と同じコードにするため)

# Create your tests here.
# from django.http import HttpRequest
from django.test import TestCase
from snippets.views import top
from django.contrib.auth import get_user_model #get_user_modelをインポート
from django.test import TestCase, Client, RequestFactory #RequestFactoryをインポート

from snippets.models import Snippet
from snippets.views import top

UserModel = get_user_model()
class TopPageRenderSnippetsTest(TestCase):
  def SetUp(self):
    self.user = UserModel.objects.create(
      username="tets_user",
      email="test@example.com",
      password="top_secret_pass0001",
    )
    self.snippet = Snippet.objects.create(
      this = "title1",
      code="print('hello')",
      description="description1",
      created_by = self.user,
    )

    def test_should_use_expected_template(self):
      response = self.client.get("/snippets/%s"%self.snippet.id)
      self.assertTemplateUsed(response, "snippets/snippet_detail.html")
    
    def test_top_page_returns_200_and_expected_heading(self):
      response = self.client.get("/snippets/%s/"%self.snippet.id)
      self.assertContains(response, self.snippet.title, status_code=200)
    def test_should_return_snippet_title(self):
      request = RequestFactory().get("/")
      request.user = self.user
      response = top(request)
      self.assertContains(response, self.snippet.title)

    def test_should_return_username(self):
      request = RequestFactory().get("/")
      request.user = self.user
      response = top(request)
      self.assertContains(response, self.user.username)
class TopPageTest(TestCase):
  def test_top_page_returns_200_and_expected_title(self):
    # request = HttpRequest() #HttpRequestオブジェクトの作成
    response = self.client.get("/")
    self.assertContains(response, "Django スニペット", status_code=200)
    # self.assertEqual(response.status_code, 200)
    def test_top_page_users_expected_template(self):
      response = self.client.get('/')
      self.assertTemplateUsed(response, "snippets/top.html")
      # self.assertEqual(response.content, b"Hello World")

class SnippetDetailTest(TestCase):
  def setUp(self):
    self.user = UserModel.object.create(
      username="test_user",
      email = "test@example.com",
      password = "secret",
    )
    self.snippet = Snippet.objects.create(
      title = "タイトル",
      code = "コード",
      description = "解説",
      created_by = self.user,
    )

    def test_should_use_expected_template(self):
      response = self.client.get("/snippets/%s"%self.snippet.id)
      self.assertTemplateUsed(response, "snippets/snippet_detail.html")
    def test_top_page_returns_200_and_expected_heading(self):
      response = self.client.get("/snippets/%s/"%self.snippet.id)
      self.assertContains(response, self.snippet.title, status_code=200)
      