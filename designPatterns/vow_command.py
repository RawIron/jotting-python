
from pyvows import Vows, expect
import command as c


@Vows.batch
class ForGuns(Vows.Context):

    class AGun(Vows.Context):
        def topic(self):
            gun = c.Gun()
            return gun
        def should_not_be_loaded(self, topic):
            expect(topic.is_loaded()).to_be_false()

    class AGunWithBullets(Vows.Context):
        def topic(self):
            gun = c.Gun()
            gun.load_the(2)
            return gun
        def should_be_loaded(self, topic):
            expect(topic.is_loaded()).to_be_true()

    class AGunWithOneBullet(Vows.Context):
        def topic(self):
            gun = c.Gun()
            gun.load_the(1)
            return gun
        def should_fire_only_once(self, topic):
            expect(topic.fire_it().is_loaded()).to_be_false()

    class AGunWithTwoBullet(Vows.Context):
        def topic(self):
            gun = c.Gun()
            gun.load_the(2)
            return gun
        def should_fire_twice(self, topic):
            expect(topic.fire_it().fire_it().is_loaded()).to_be_false()

