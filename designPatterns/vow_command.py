
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
            gun.load_with(2)
            return gun
        def should_be_loaded(self, topic):
            expect(topic.is_loaded()).to_be_true()

    class AGunWithOneBullet(Vows.Context):
        def topic(self):
            gun = c.Gun()
            gun.load_with(1)
            return gun
        def should_fire_only_once(self, topic):
            expect(topic.fire_it().is_loaded()).to_be_false()

    class AGunWithTwoBullets(Vows.Context):
        def topic(self):
            gun = c.Gun()
            gun.load_with(2)
            return gun
        def should_fire_twice(self, topic):
            expect(topic.fire_it().fire_it().is_loaded()).to_be_false()


@Vows.batch
class ForTargets(Vows.Context):
    
    class ATarget(Vows.Context):
        def topic(self):
            target = c.Target()
            return target
        def should_be_healthy_when_created(self, topic):
            expect(topic.is_destroyed()).to_be_false()

    class ATargetHitByLargerForceThanHealth(Vows.Context):
        def topic(self):
            target = c.Target()
            target.got_hit_by(6)
            return target
        def should_be_destroyed(self, topic):
            expect(topic.is_destroyed()).to_be_true()

    class ATargetHitBySmallerForceThanHealth(Vows.Context):
        def topic(self):
            target = c.Target()
            target.got_hit_by(4)
            return target
        def should_not_be_destroyed(self, topic):
            expect(topic.is_destroyed()).to_be_false()


@Vows.batch
class ForCommandServers(Vows.Context):
    
    class ACommandServer(Vows.Context):
        def topic(self):
            server = c.Server()
            return server
        def should_do_nothing(self, topic):
            expect(topic.run().has()).to_be_false()

    class ACommandServerGivenNotACommand(Vows.Context):
        def topic(self):
            server = c.Server()
            server.sent(3)
            return server
        def should_not_run_it(self, topic):
            expect(topic.run()).to_be_an_error_like(AttributeError)

    class ACommandServerGivenACommand(Vows.Context):
        def topic(self):
            gun = c.Gun()
            command = c.GunFireCommand(gun)
            server = c.Server()
            server.sent(command)
            return server
        def should_have_it(self, topic):
            expect(topic.has()).to_be_true()
        def should_run_it_and_then_remove_it(self, topic):
            expect(topic.run().has()).to_be_false()


