#!/usr/bin/env python
# -*- coding: utf-8 -*-

from neutron.common import exceptions as exc
from neutron.plugins.ml2.driver_api import TypeDriver
from neutron.plugins.ml2 import driver_api as api

import logging
LOG = logging.getLogger(__name__)

class SangwookTypeDriver(TypeDriver):

    def __init__(self):
        LOG.info('sangwooklogtest: __init__')

    def get_type(self):
        return 'sangwooktype'

    def initialize(self):
        pass

    def is_partial_segment(self, segment):
        return False

    def validate_provider_segment(self, segment):
        for key, value in segment.iteritems():
            if value and key != api.NETWORK_TYPE:
                msg = _("%s prohibited for sangwook provider network") % key
                raise exc.InvalidInput(error_message=msg)

    def reserve_provider_segment(self, session, segment):
        return segment

    def allocate_tenant_segment(self, session):
        return {api.NETWORK_TYPE: 'sangwooktype'}

    def release_segment(self, session, segment):
        pass
