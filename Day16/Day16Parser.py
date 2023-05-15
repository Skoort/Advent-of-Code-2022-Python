import re

from Day16.Day16Solver import Day16Solver
from Day16.ZooSettings import ZooSettings
from Shared.Parser import Parser


class Day16Parser(Parser):
    def get_solver(self, text: str) -> Day16Solver:
        name_to_index = {}
        for i, line in enumerate(text.strip().split('\n')):
            match = re.search('Valve (?P<name>.*) has flow rate=(?P<flow_rate>.*); tunnel(s)? lead(s)? to valve(s)? (?P<connections>.*)', line)
            name = match.group('name')
            name_to_index[name] = i
        index_to_name = {v: k for k, v in name_to_index.items()}

        valves = {}
        for i, line in enumerate(text.strip().split('\n')):
            match = re.search('Valve (?P<name>.*) has flow rate=(?P<flow_rate>.*); tunnel(s)? lead(s)? to valve(s)? (?P<connections>.*)', line)
            flow_rate = int(match.group('flow_rate'))
            connections = [name_to_index[t.strip()] for t in match.group('connections').split(',')]
            valves[i] = (flow_rate, connections)

        start_valve_index = name_to_index['AA']

        return Day16Solver(ZooSettings(valves, name_to_index, index_to_name, start_valve_index))
