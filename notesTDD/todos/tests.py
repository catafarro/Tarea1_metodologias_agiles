from django.test import TestCase
from todos.models import *
# Create your tests here.

class TestTodoCreate(TestCase):

    # Dado el Contexto (Given)
    def setUp(self):        
        Todo.objects.create(name="todo1")

    def test(self):
        Todo.objects.create(name='todo2')
        self.assertEqual(Todo.objects.get(name="todo2").name ,'todo2')



class TestTodoEdit(TestCase):

    def setUp(self):
        Todo.objects.create(name="todo3", description="esta es la tarea 3")
        Todo.objects.create(name="todo4", description="test")

    def test1(self):    
        nuevat3 = Todo.objects.get(name="todo3")
        nuevat3.description = "esta es la nueva tarea 3"
        nuevat3.save()
        self.assertEqual(Todo.objects.get(name="todo3").description, "esta es la nueva tarea 3")

    def test2(self):
        nuevat4 = Todo.objects.get(name="todo4")
        nuevat4.name = "tarea4"
        nuevat4.save()
        self.assertEqual(Todo.objects.get(name="tarea4").name, "tarea4")