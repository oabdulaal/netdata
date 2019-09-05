# -*- coding: utf-8 -*-
# Description: s_tui netdata python.d module
# Author: Omar Mahmoud
# SPDX-License-Identifier: GPL-3.0-or-later

from bases.FrameworkServices.SimpleService import SimpleService
from bases.collection import find_binary
from subprocess import Popen, PIPE
import json

disabled_by_default = False

priority = 90000

STUI = 's-tui'

ORDER = [
    'power',
    'temperature',
]

CHARTS = {
    'power': {
        'options': [None, 'CPU Power consumption', 'Watts', 'stui', 'stui.power', 'line'],
        'lines': [
            ['power', None, 'absolute']
        ]
    },
    'temperature': {
        'options': [None, 'CPU temperature', 'C', 'stui', 'stui.temperature', 'line'],
        'lines': [
            ['temperature', None, 'absolute']
        ]
    }
}


class Service(SimpleService):
    def __init__(self, configuration=None, name=None):
        SimpleService.__init__(self, configuration=configuration, name=name)
        self.order = ORDER
        self.definitions = CHARTS
        self.stui = find_binary(STUI)
        self.stui_command = [self.stui, '--json']

    def check(self):
        if not self.stui:
            self.error('can\'t locate "{0}" binary'.format(STUI))
            return False
        return True

    def _get_data(self):
        try:
            p = Popen(self.stui_command, stdout=PIPE, stderr=PIPE)
        except Exception as error:
            self.error('Executing command {command} resulted in error: {error}'.format(command=self.stui_command, error=error))
        data = str()
        std = p.stdout
        for line in std:
            try:
                data += str(line.decode('utf-8'))
            except TypeError:
                self.debug('Type error in line: {line}')
        data_json = json.loads(data)
        cur_power = float(data_json["Cur Power"][0:-1])
        cur_temp = float(data_json["Cur Temp"][0:-1])
        # print("DATA: ", cur_power, cur_temp)
        return {'power': cur_power,
                'temperature': cur_temp}
        
