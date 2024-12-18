# Generated by Grammarinator 23.7

import itertools

from math import inf
from grammarinator.runtime import *

class userAPIGenerator(Generator):


    def EOF(self, parent=None):
        pass
    EOF.min_depth = 0

    def userAPI(self, parent=None):
        with RuleContext(self, UnparserRule(name='userAPI', parent=parent)) as current:
            self.email(parent=current)
            UnlexerRule(src='\n', parent=current)
            self.isActive(parent=current)
            UnlexerRule(src='\n', parent=current)
            self.fullName(parent=current)
            UnlexerRule(src='\n', parent=current)
            self.password(parent=current)
            UnlexerRule(src='\n', parent=current)
            self.username(parent=current)
            UnlexerRule(src='\n', parent=current)
            self.isSuperuser(parent=current)
            UnlexerRule(src='\n', parent=current)
            self.EOF(parent=current)
            return current
    userAPI.min_depth = 2

    def email(self, parent=None):
        with RuleContext(self, UnparserRule(name='email', parent=parent)) as current:
            with AlternationContext(self, [1, 1, 1, 1], [1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.EMPTY_EMAIL, self.MISSING_AT, self.MISSING_DOMAIN, self.VALID_EMAIL][choice0](parent=current)
            return current
    email.min_depth = 1

    def EMPTY_EMAIL(self, parent=None):
        with RuleContext(self, UnlexerRule(name='EMPTY_EMAIL', parent=parent)) as current:
            UnlexerRule(src=' ', parent=current)
            return current
    EMPTY_EMAIL.min_depth = 0

    def MISSING_AT(self, parent=None):
        with RuleContext(self, UnlexerRule(name='MISSING_AT', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[1]), parent=current)
            UnlexerRule(src=' ', parent=current)
            return current
    MISSING_AT.min_depth = 0

    def MISSING_DOMAIN(self, parent=None):
        with RuleContext(self, UnlexerRule(name='MISSING_DOMAIN', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[2]), parent=current)
            UnlexerRule(src='@', parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 1, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 1, self._charsets[3]), parent=current)
            UnlexerRule(src=' ', parent=current)
            return current
    MISSING_DOMAIN.min_depth = 0

    def VALID_EMAIL(self, parent=None):
        with RuleContext(self, UnlexerRule(name='VALID_EMAIL', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[4]), parent=current)
            UnlexerRule(src='@', parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 1, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 1, self._charsets[5]), parent=current)
            UnlexerRule(src='.', parent=current)
            with AlternationContext(self, [0, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['com', 'org'][choice0], parent=current)
            return current
    VALID_EMAIL.min_depth = 0

    def isActive(self, parent=None):
        with RuleContext(self, UnparserRule(name='isActive', parent=parent)) as current:
            with AlternationContext(self, [0, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['true', 'false'][choice0], parent=current)
            return current
    isActive.min_depth = 0

    def fullName(self, parent=None):
        with RuleContext(self, UnparserRule(name='fullName', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    self.ALPHANUMERIC(parent=current)
            return current
    fullName.min_depth = 1

    def password(self, parent=None):
        with RuleContext(self, UnparserRule(name='password', parent=parent)) as current:
            with AlternationContext(self, [1, 1], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    self.EMPTY_PASSWORD(parent=current)
                elif choice0 == 1:
                    self.ALPHANUMERIC(parent=current)
                    if self._max_depth >= 1:
                        for _ in self._model.quantify(current, 0, min=0, max=inf):
                            with AlternationContext(self, [1, 1], [1, 1]) as weights1:
                                choice1 = self._model.choice(current, 1, weights1)
                                [self.ALPHANUMERIC, self.SPECIAL_CHARACTERS][choice1](parent=current)
            return current
    password.min_depth = 1

    def EMPTY_PASSWORD(self, parent=None):
        with RuleContext(self, UnlexerRule(name='EMPTY_PASSWORD', parent=parent)) as current:
            UnlexerRule(src=' ', parent=current)
            return current
    EMPTY_PASSWORD.min_depth = 0

    def username(self, parent=None):
        with RuleContext(self, UnparserRule(name='username', parent=parent)) as current:
            with AlternationContext(self, [1, 1], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    self.EMPTY_USERNAME(parent=current)
                elif choice0 == 1:
                    if self._max_depth >= 0:
                        for _ in self._model.quantify(current, 0, min=1, max=inf):
                            self.ALPHANUMERIC(parent=current)
            return current
    username.min_depth = 1

    def EMPTY_USERNAME(self, parent=None):
        with RuleContext(self, UnlexerRule(name='EMPTY_USERNAME', parent=parent)) as current:
            UnlexerRule(src=' ', parent=current)
            return current
    EMPTY_USERNAME.min_depth = 0

    def isSuperuser(self, parent=None):
        with RuleContext(self, UnparserRule(name='isSuperuser', parent=parent)) as current:
            with AlternationContext(self, [0, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['true', 'false'][choice0], parent=current)
            return current
    isSuperuser.min_depth = 0

    def ALPHANUMERIC(self, parent=None):
        with RuleContext(self, UnlexerRule(name='ALPHANUMERIC', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[6]), parent=current)
            return current
    ALPHANUMERIC.min_depth = 0

    def SPECIAL_CHARACTERS(self, parent=None):
        with RuleContext(self, UnlexerRule(name='SPECIAL_CHARACTERS', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[7]), parent=current)
            return current
    SPECIAL_CHARACTERS.min_depth = 0

    _default_rule = userAPI

    _charsets = {
        0: list(itertools.chain.from_iterable([range(32, 127)])),
        1: list(itertools.chain.from_iterable([range(37, 38), range(43, 44), range(45, 46), range(46, 47), range(48, 58), range(65, 91), range(95, 96), range(97, 123)])),
        2: list(itertools.chain.from_iterable([range(37, 38), range(43, 44), range(45, 46), range(46, 47), range(48, 58), range(65, 91), range(95, 96), range(97, 123)])),
        3: list(itertools.chain.from_iterable([range(45, 46), range(46, 47), range(48, 58), range(65, 91), range(97, 123)])),
        4: list(itertools.chain.from_iterable([range(37, 38), range(43, 44), range(45, 46), range(46, 47), range(48, 58), range(65, 91), range(95, 96), range(97, 123)])),
        5: list(itertools.chain.from_iterable([range(45, 46), range(46, 47), range(48, 58), range(65, 91), range(97, 123)])),
        6: list(itertools.chain.from_iterable([range(48, 58), range(65, 91), range(97, 123)])),
        7: list(itertools.chain.from_iterable([range(32, 34), range(35, 48), range(58, 65), range(91, 97), range(123, 127)])),
    }
