
from pyvows import Vows, expect
from observer import *


@Vows.batch
class Achievements(Vows.Context):

    class AnAchievement(Vows.Context):
        def topic(self):
            return Achievement()

        def should_not_be_free(self, topic):
            expect(topic.isEarned()).Not.to_be_true()


        class ForAGunFiredOnce(Vows.Context):
            def topic(self, achievement):
                g = Gun()
                g.subscribe(achievement)
                g.fire()
                return achievement

            def should_not_be_given(self, topic):
                expect(topic.check()).Not.to_be_true()

