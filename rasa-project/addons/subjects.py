from rasa.core.slots import Slot
from actions.action_utils import subjects


class Subjects_1(Slot):

    def feature_dimensionality(self):
        return len(subjects)

    def as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        for i, v in enumerate(subjects):
            if self.value == v:
                r[i] = 1.0
        return r
