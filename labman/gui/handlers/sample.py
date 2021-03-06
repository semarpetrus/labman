# ----------------------------------------------------------------------------
# Copyright (c) 2017-, labman development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from tornado.web import authenticated
from tornado.escape import json_encode

from labman.gui.handlers.base import BaseHandler
from labman.db.composition import SampleComposition


class ControlSamplesHandler(BaseHandler):
    @authenticated
    def get(self):
        term = self.get_argument('term', None)
        self.write(json_encode(SampleComposition.get_control_samples(term)))
        self.finish()
