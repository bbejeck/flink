# ###############################################################################
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
# limitations under the License.
################################################################################
from flink.functions import Function


class FlatMapFunction(Function.Function):
    def __init__(self):
        super(FlatMapFunction, self).__init__()

    def _run(self):
        collector = self._collector
        function = self.flat_map
        iterator = self._iterator
        for value in iterator:
            result = function(value, collector)
            if result is not None:
                for res in result:
                    collector.collect(res)
        collector._close()

    def collect(self, value):
        collector = self._collector
        result = self.flat_map(value, collector)
        if result is not None:
            for res in result:
                collector.collect(res)

    def flat_map(self, value, collector):
        pass