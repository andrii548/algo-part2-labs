class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_customer(self, customer):
        new_node = Node(customer)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def serve_next(self):
        if not self.is_empty():
            served_customer = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
        else:
            served_customer = None
        return served_customer

    def show_queue(self):
        print("Current queue:")
        current = self.front

        while current is not None:
            print(current.data)
            current = current.next

    def is_empty(self):
        return self.front is None
