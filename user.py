#user.py
from library import Base


assert hasattr(Base,'foo'), "you  broke it, you fool!"

class Derived(Base):
    def bar(self):
        return self.foo()


a = Derived()
print(a.bar())