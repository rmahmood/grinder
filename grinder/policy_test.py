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

import time
import pytest
from threading import Thread

from . import harness
from . logger import log
from . import requirements
from . import instance

class TestPolicy(harness.TestCase):

    @harness.requires(requirements.INSTALL_POLICY)
    @harness.platformtest(only=["linux"])
    def test_memory_limit_enforcement(self, image_finder):
        with self.harness.blessed(image_finder) as blessed:
            # For now we only run this test on linux VMs because linux VMs
            # stabilize at very small memory footprint after a launch.

            # Prepare a policy for this domain where it's memory limit will be
            # enforced.
            self.harness.policy += \
"""
[*;blessed=%s;*]
memory_limit_mb = 256
""" % blessed.id

            with harness.locked_policy():
                self.harness.install_policy()

            stop_checking = False
            def check_memory_usage(control, memory_threshold):
                """ Ensure the memory usage of the domain doesn't
                while not stop_checking:
                    assert int(control.get_param("memory.current")) <= \
                        memory_threshold
                    time.sleep(1.0)





            # Launch a new instance an try to push it's memory above the limit
            # we just set. The memory used should never significantly exceed the
            # memory limit. We expect vmspolicyd to activate eviction during
            # this exercise. This test also ensures that a throttled VM
            # continues to make progress and will eventually complete any memory
            # intensive task (once eviction catches up).
            launched = blessed.launch()
            launched.allocate_balloon(256 * 256)
