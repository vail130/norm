from __future__ import absolute_import
from __future__ import print_function

from norm.base import Base
from norm.column import Column


class Table(Base):
    def __init__(self, name, subquery=None):
        self._name = name
        self._subquery = subquery
        self._as = None
        self._on = None

    def __getattr__(self, item):
        return Column(item, table=self)

    def AS(self, alias):
        self._as = alias
        return self

    def ON(self, *args):
        self._on = args
        return self

    def _to_string(self):
        output = u'%s' % self._name

        if self._as is not None:
            output = u'%s AS %s' % (output, self._as)
        elif self._on is not None:
            output = u'%s ON' % output
            for on in self._on:
                output = u'%s %s' % (output, on)

        return output
