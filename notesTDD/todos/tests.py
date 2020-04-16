from django.test import TestCase
from todos.models import *
# Create your tests here.

class TestTodo(TestCase):

    # Dado el Contexto (Given)
    def setUp(self):        
        Todo.objects.create(name="todo1")

    def test_agregar_tarea(self):
        Todo.objects.create(name='todo2')
        self.assertEqual(Todo.objects.get(name="todo2").name ,'todo2')