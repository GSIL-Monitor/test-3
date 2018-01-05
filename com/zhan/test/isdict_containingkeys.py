from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.core.helpers.wrap_matcher import wrap_matcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsDictContainingKeys(BaseMatcher):

    def __init__(self, key_matcher):
        self.key_matcher = key_matcher

    def _matches(self, dictionary):
        if hasmethod(dictionary, 'keys'):
            expkeys = self.key_matcher.split(',')
            for expkey in expkeys:
                if expkey not in dictionary.keys():
                    return False
            return True
        else:
            return False

    def describe_to(self, description):
        description.append_text('a dictionary containing keys ')     \
                    .append_description_of(self.key_matcher)


def has_keys(key_match):
    return IsDictContainingKeys(key_match)
    # return IsDictContainingKeys(wrap_matcher(key_match))
