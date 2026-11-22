class Parentclass:
    def parent_method(self):
        print("This is the parent method.")
class Childclass(Parentclass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = Childclass()
child_object.child_method()