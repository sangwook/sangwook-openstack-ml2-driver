#!/usr/bin/env python
# -*- coding: utf-8 -*-

from neutron.plugins.ml2.driver_api import MechanismDriver

import logging
LOG = logging.getLogger(__name__)

class SangwookMechanismDriver(MechanismDriver):

    def __init__(self):
        LOG.info('sangwooklogtest: __init__')
        pass

    def initialize(self):
        pass

