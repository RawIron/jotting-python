
from pyvows import Vows, expect

class ClassesThatInheritFromSuperclass(Vows.Context):
    def topic(self):

    def cannot_overload(self, topic):

    def cannot_overwrite(self, topic):

    def can_see_underscored_names(self, topic):



class ClassesWithoutInit(Vows.Context):
    def topic(self):
        class no_init(object):
            self.no_init
            self.global = 23
            def change(self):
                self.global = 1
            def read(self):
                return self.global

    def cannot_read_self_globals(self, topic):

    def do_not_have_a_state(self, topic):

    def can_create_object_variables_dynamically(self, topic):


class ForNestedKlasses(Vows.Context):
    def topic(self):
        class outer(object):
            self.value = False
            def method(self):
                return self.value

            class inner():
                self.value = True
                def method(self):
                    return self.value
        return outer()

    def inner_klass_isa_outer_klass(self, topic):
        expect(topic.).is_instance_of()

    def inner_klass_accesses_outer_klass_by(self, topic):
        expect(topic.).is_true()

    def inner_klass_can_write_outer_klass(self, topic):
        expect(topic.).


class KlassesWithStaticMethod(Vows.Context):
    def topic(self):
        class A(object):
            BWithStatic.call()
            @staticmethod
            def call():
                print "called A"

        class BWithStatic(object):
            @staticmethod
            def call():
                print "called B"

    def enforce_order_in_declaration(self, topic):
        expect(topic()).to_raise()

