
from pyvows import Vows, expect
import pylibmc

memcache_server = ["127.0.0.1", ]
memc = pylibmc.Client(memcache_server, binary=True,
                      behaviors={"tcp_nodelay": True, "ketama": True})


@Vows.batch
class Caches(Vows.Context):
    class ACacheConnection(Vows.Context):
        def topic(self):
            return memc
        def should_be_available(self, topic):
            expect(topic.set("test_", "dummy", 3)).to_be_true()
        def should_not_require_authentication(self, topic)
            pass

    class ACacheGet(Vows.Context):
        def topic(self):
            return memc.get("test_")
        def should_return_the_data_for_key(self, topic):
            expect(topic.

    class ACacheSetWithExpire(Vows.Context):
        pass

