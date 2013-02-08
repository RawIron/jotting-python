
from pyvows import Vows, expect


@Vows.batch
class NestedFunctions(Vows.Context):
    def topic(self):
        def do():
            def in_do(job):
                return "did %s" % job

            job = "first job"
            return in_do(job)
        return do

    def can_be_called_from_outer(self, topic):
        expect(topic()).to_equal("did first job")


@Vows.batch
class ImportInFunctionBlock(Vows.Context):
    def topic(self):
        def import_os():
            import os
        return os.name

    def is_not_visible_outside_block(self, topic):
        expect(topic).to_be_an_error_like(NameError)

