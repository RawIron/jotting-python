
from pyvows import Vows, expect


class InitPy(Vows.Context):
    class InThePackageRootUsingImport():
        def topic(self):
            import gotchas

        def it_should_(self, topic):
            expect(topic.name).to_not_exist()

        def it_should_show_private_identifiers(self, topic):
            expect(topic._name).to_not_exist()

