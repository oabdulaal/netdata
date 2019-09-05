# -*- coding: utf-8 -*-
# Description: powertop netdata python.d module
# Author: Omar Mahmoud, Mahmoud Nabegh
# SPDX-License-Identifier: GPL-3.0-or-later

from bases.FrameworkServices.SimpleService import SimpleService
from bases.collection import find_binary
from bs4 import BeautifulSoup
import re
import sys, os
from subprocess import Popen, PIPE

disabled_by_default = False

priority = 90000

SUDO = 'sudo'

POWERTOP = 'powertop'

CAT = 'cat'

ORDER = [
    'processes'
]

CHARTS = {
    'processes': {
        'options': [None, 'Powertop processes', 'ms/s', 'powertop', 'powertop.processes', 'line'],
        'lines': [
            []
        ]
    }
}


class Service(SimpleService):
    def __init__(self, configuration=None, name=None):
        SimpleService.__init__(self, configuration=configuration, name=name)
        self.base_path = os.path.dirname(sys.argv[0])
        self.html_path = self.base_path + "/powertop.html"
        self.debug("Called super..")
        self.order = ORDER
        self.definitions = CHARTS

        self.sudo = find_binary(SUDO)
        self.powertop = find_binary(POWERTOP)
        self.cat = find_binary(CAT)
        self.powertop_command = [self.sudo, '-n', self.powertop, '--time=1', '-q', '--html=' + self.html_path]
        self.cat_command = [self.sudo, self.cat, self.html_path]
        self.use_sudo = True

    def check(self):
        if not self.sudo:
            self.error('can\'t locate "{0}" binary'.format(SUDO))
            return False
        if not self.cat:
            self.error('can\'t locate "{0}" binary'.format(CAT))
            return False
        if not self.powertop:
            self.error('can\'t locate "{0}" binary'.format(POWERTOP))
            return False
        return True

    def update_processes_chart(self, processes):
        if not processes:
            return
        chart = self.charts['processes']
        active_dim_ids = []
        for p in processes:
            dim_id = p["PID"]
            active_dim_ids.append(dim_id)
            if dim_id not in chart:
                chart.add_dimension([dim_id, dim_id, 'absolute'])
        for dim in chart:
            if dim.id not in active_dim_ids:
                chart.del_dimension(dim.id, hide=False)

    def _get_data(self):
        self.debug("Getting data ..")
        try:
            p = Popen(self.powertop_command, stdout=PIPE, stderr=PIPE)
        except Exception as error:
            self.error('Executing command {command} resulted in error: {error}'.format(command=self.powertop_command, error=error))

        try:
            p = Popen(self.cat_command, stdout=PIPE, stderr=PIPE)
        except Exception as error:
            self.error('Executing command {command} resulted in error: {error}'.format(command=self.cat_command, error=error))
        data = str()
        std = p.stdout
        for line in std:
            try:
                data += str(line.decode('utf-8'))
            except TypeError:
                self.debug('Type error in line: {line}')
      
        soup = BeautifulSoup(data, 'html.parser')
        counter = 0
        res = []
        ret_obj = {}
        for child in soup.body.find("div", {"id": "software"}).table.children:
            if hasattr(child, 'children'):
                if counter != 0:
                    usage = child.contents[1].string.strip()
                    categ = child.contents[-4].string.strip()
                    desc = child.contents[-2].string.strip()

                    if(categ == "Process"):
                        pid = re.search("[0-9]+", desc).group()
                        value = float(re.search("[0-9]+[.][0-9]+", usage).group())
                        microsec = re.search("us", usage)
                        if microsec is not None:
                            value = value/float(1000)
                        res.append({'Usage': value, 'PID': pid})
                        ret_obj[pid] = value

                counter += 1
        res = sorted(res, key=lambda k: k['Usage'], reverse=True) 
        self.update_processes_chart(res)
        return ret_obj
        
