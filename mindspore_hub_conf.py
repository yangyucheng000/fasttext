#   d
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""hub config"""
from src.fasttext_model import FastText

def fasttext(*args, **kwargs):
    return FastText(*args, **kwargs)


def create_network(name, *args, **kwargs):
    if name == "fasttext":
        return FastText(*args, **kwargs)
    raise NotImplementedError(f"{name} is not implemented in the repo")
