# Copyright 2013 GridCentric Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import gridcentric_python_novaclient_ext

class NovaClientCapability(object):

    def __init__(self, capability):
        self.capability = capability

    def check(self, client):
        return client.gridcentric.satisfies([self.capability])

LAUNCH_NAME = NovaClientCapability('launch-name')

USER_DATA = NovaClientCapability('user-data')

SECURITY_GROUPS = NovaClientCapability('security-groups')

AVAILABILITY_ZONE = NovaClientCapability('availability-zone')
