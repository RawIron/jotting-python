
from pyvows import Vows, expect


@Vows.batch
class KlassesThatInheritFromSuperklass(Vows.Context):

    def topic(self):
        class SuperKlass(object):
            def parent_method(self):
                return True
            def _invisible(self):
                return False

        class SubKlass(SuperKlass):
            def parent_method(self):
                return False

        return SubKlass()

    def can_override(self, topic):
        expect(topic.parent_method()).to_be_false()

    def can_see_underscored_names(self, topic):
        expect(topic._invisible()).to_be_false()


@Vows.batch
class KlassesWithoutInit(Vows.Context):

    def topic(self):
        class NoInit(object):
            no_init = None
            klass_variable = 23
            def change(self):
                self.klass_variable = 1
            def read(self):
                return self.klass_variable
            def new_variable(self):
                self.dynamic = True
                return self._is_it_there()
            def _is_it_there(self):
                return self.dynamic
        return NoInit()

    def can_read_self_globals(self, topic):
        expect(topic.read()).to_equal(23)

    def can_access_klass_variables(self, topic):
        expect(topic.no_init).to_be_null()

    def can_create_object_variables_dynamically(self, topic):
        expect(topic.new_variable()).to_be_true()



@Vows.batch
class ForNestedKlasses(Vows.Context):

    def topic(self):
        class Outer(object):
            def __init__(self):
                self.value = False
            def method(self):
                return self.value

            class Inner(object):
                def __init__(self):
                    self.inner_value = True
                def inner_method(self):
                    return self.inner_value
        return Outer.Inner()

    def inner_klass_cannot_access_outer_klass(self, topic):
        expect(topic.method()).to_be_an_error()

    def inner_klass_cannot_write_outer_klass(self, topic):
        expect(topic.value).to_be_an_error()



@Vows.batch
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
        expect(topic).to_be_an_error()


