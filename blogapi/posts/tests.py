from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogTests(TestCase):
    @classmethod

    def setUpTestData(cls):
        jacobnewton = User.objects.create(
            username = 'jacobnewton',
            password = 'abc123')
        jacobnewton.save()

        test_post = Post.objects.create(
            author=jacobnewton, title= 'Blog title', body = 'Body content...'
        )
        test_post.save()


    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEquals(author, 'jacobnewton')
        self.assertEquals(title, 'Blog title')
        self.assertEquals(body, 'Body content...')
    # def setUpTestData(cls):
    #     # Create a user
    #     testuser1 = User.objects.create_user(
    #     username='testuser1', password='abc123')
    #     testuser1.save()
    # # Create a blog post
    #     test_post = Post.objects.create(
    #     author=testuser1, title='Blog title', body='Body content...')
    #     test_post.save()
    # def test_blog_content(self):
    # post = Post.objects.get(id=1)
    # author = f'{post.author}'
    # title = f'{post.title}'
    # body = f'{post.body}'
    # self.assertEqual(author, 'testuser1')
    # self.assertEqual(title, 'Blog title')
    # self.assertEqual(body, 'Body content...')