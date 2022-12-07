from Day07.Day07Solver import Day07Solver
from Day07.Directory import Directory
from Day07.File import File
from Shared.Parser import Parser


class Day07Parser(Parser):
    def get_solver(self, text: str) -> Day07Solver:
        root_dir = None
        current_dir = None
        is_reading_files = False
        lines = text.strip().split('\n')
        for line in lines:
            if line[0] == '$':
                args = line.replace('$', '').strip().split()
                if args[0] == 'ls':
                    is_reading_files = True
                elif args[0] == 'cd':
                    is_reading_files = False
                    if current_dir is None:
                        current_dir = Directory(args[1], None)
                        root_dir = current_dir
                    else:
                        current_dir = current_dir.get(args[1])
            elif is_reading_files:
                arg1, name = line.split()
                if arg1 == 'dir':
                    current_dir.contents[name] = Directory(name, current_dir)
                else:
                    current_dir.contents[name] = File(name, int(arg1), current_dir)
        return Day07Solver(root_dir)
