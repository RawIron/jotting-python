
from pyvows import Vows, expect

@Vows.batch
class InitPy(Vows.Context):
    class InThePackageRootUsingImport():
        def topic(self):
            import gotchas
            return gotchas

        def it_should_(self, topic):
            expect(topic.name).to_be_an_error_like(AttributeError)

        def it_should_show_private_identifiers(self, topic):
            expect(topic._name).to_be_an_error_like(AttributeError)

