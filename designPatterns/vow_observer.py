
from pyvows import Vows, expect
from observer import *


@Vows.batch
class Achievements(Vows.Context):

    class AnAchievement(Vows.Context):
        def topic(self):
            return Achievement()

        def should_not_be_free(self, topic):
            expect(topic.is_earned()).to_be_false()


        # async processing breaks the two vows below (!)
        class ForAGunFiredOnce(Vows.Context):
            def topic(self, achievement):
                g = Gun()
                g.subscribe(achievement)
                g.fire()
                return achievement

            def should_not_be_given(self, topic):
                expect(topic.is_earned()).to_be_false()


        class ForAGunFiredTwice(Vows.Context):
            def topic(self, achievement):
                g = Gun()
                g.subscribe(achievement)
                g.fire()
                g.fire()
                return achievement

            def should_be_given(self, topic):
                expect(topic.is_earned()).to_be_true()




@Vows.batch
class Guns(Vows.Context):
    class AGun(Vows.Context):
        def topic(self):
            return Gun()

        def should_be_loaded(self, topic):
            expect(topic.loaded()).to_be_true()


