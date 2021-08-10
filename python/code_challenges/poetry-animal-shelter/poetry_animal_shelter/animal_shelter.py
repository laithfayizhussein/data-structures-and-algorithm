

class Node:
    def __init__(self, value):

        self.value=value
        self.next=None

class Queue:
    def __init__(self):

        self.front=None
        self.rear=None

    def enqueue(self, value):
        node = Node(value)

        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
           dequeue_value=self.front.value
           self.front=self.front.next
           return dequeue_value
        except :
           return ' empty Queue '

class Dog:

    def __init__(self,name):
        self.name=name
        self.kind='dog'

class Cat:

    def __init__(self,name):
        self.name=name
        self.kind='cat'

class Animal:

    def __init__(self,name,kind):
        self.name=name
        self.kind=kind


class Animalshelter:

    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self,animal):

        if animal.kind=='cat':
            self.cat.enqueue(animal)
        elif animal.kind=='dog':
            self.dog.enqueue(animal)
        else:

            return 'the animal should be cat or dog'

    def dequeue(self,pref=None):

        if pref == 'cat':
            return self.cat.dequeue().name
        elif pref == 'dog':
            return self.dog.dequeue().name
        else:
            return None





if __name__ == "__main__":
    wolf = Dog('wolf')
    riex=Dog('riex')
    lolo = Cat('lolo')
    sinp=Cat('sinp')
    lion=Animal('lion','snake')
    ash=Animalshelter()
    ash.enqueue(wolf)
    ash.enqueue(riex)
    ash.enqueue(lolo)
    ash.enqueue(sinp)
    print(ash.enqueue(lion))
    print(ash.dequeue('cat'))
