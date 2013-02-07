
from pyvows import Vows, expect


class NestedFunctions(Vows.Context):
    def topic(self):
        def do():
            def in_do(job):
                return "did %s" % job

            job = "first job"
            return in_do(job)

    def can_be_called_from_outer(self, topic):
        expect(topic.do()).to_equal("did first job")


class ImportInFunctionBlock(Vows.Context):
    def topic(self):
        def import_os():
            import os
        return os.name

    def is_not_visible_outside_block(self, topic):
        try:
            expect(topic().to_raise(NameError)
        except NameError:
            print "os not known outside the block"

