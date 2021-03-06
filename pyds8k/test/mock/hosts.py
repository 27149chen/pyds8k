##############################################################################
# Copyright 2019 IBM Corp.
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
##############################################################################

ALL = {
    "server": {
        "status": "ok",
        "code": "CMUC00183I",
        "message": "Operation done successfully."
    },
    "counts": {
        "data_counts": 32,
        "total_counts": 32
    },
    'data': {
        'hosts': [
            {
                'name': 'host1',
                'state': 'Online',
                'hosttype': 'VMWare',
                'addrmode': 'SCSI map',
                'addrdiscovery': 'Report LUNs',
                'lbs': '512',
                'host_ports': {
                    'link': {
                        'rel': 'self',
                        'href': 'https://localhost:8088/api/v1/host_ports',
                    },
                },
                'ioports': {
                    'link': {
                        'rel': 'self',
                        'href': 'https://localhost:8088/api/v1/ioports',
                    },
                },
                'volumes': {
                    'link': {
                        'rel': 'self',
                        'href': 'https://localhost:8088/api/v1/volumes',
                    },
                },
                'link': {
                    'rel': 'self',
                    'href': 'https://localhost:8088/api/v1/hosts/host1'
                },
            },
            {
                'name': 'host2',
                'state': 'Online',
                'hosttype': 'VMware',
                'addrmode': 'SCSI map',
                'addrdiscovery': 'Report LUNs',
                'lbs': '512',
                'host_ports': {
                    'link': {
                        'rel': 'self',
                        'href': 'https://localhost:8088/api/v1/host_ports',
                    },
                },
                'ioports': {
                    'link': {
                        'rel': 'self',
                        'href': 'https://localhost:8088/api/v1/ioports',
                    },
                },
                'volumes': {
                    'link': {
                        'rel': 'self',
                        'href': 'https://localhost:8088/api/v1/volumes',
                    },
                },
                'link': {
                    'rel': 'self',
                    'href': 'https://localhost:8088/api/v1/hosts/host2'
                },
            },
        ]
    }
}

ONE = {
    "server": {
        "status": "ok",
        "code": "CMUC00183I",
        "message": "Operation done successfully."
    },
    "counts": {
        "data_counts": 1,
        "total_counts": 1
    },
    'data': {
        'hosts': [
            {
                'name': 'host1',
                'state': 'Online',
                'hosttype': 'VMWare',
                'addrmode': 'SCSI map',
                'addrdiscovery': 'Report LUNs',
                'lbs': '512',
                'host_ports': {
                    'link': {
                        'rel': 'self',
                        'href': 'https://localhost:8088/api/v1/host_ports',
                    },
                },
                'ioports': {
                    'link': {
                        'rel': 'self',
                        'href': 'https://localhost:8088/api/v1/ioports',
                    },
                },
                'volumes': {
                    'link': {
                        'rel': 'self',
                        'href': 'https://localhost:8088/api/v1/volumes',
                    },
                },
                'link': {
                    'rel': 'self',
                    'href': 'https://localhost:8088/api/v1/hosts/host1'
                },
            },
        ]
    }
}
