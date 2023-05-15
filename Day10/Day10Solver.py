from Shared.Solver import Solver, Part


class Day10Solver(Solver):
    def __init__(self, instructions: list[((str, tuple[str]))]):
        self.__instructions = instructions

    def solve(self, part: Part) -> str:
        total_signal_strength = 0
        screen_buffer = [False for _ in range(40*6)]

        register_x = 1

        instruction_index = 0
        next_cycle = 1

        command = None
        args = tuple()

        cycle = 1
        while instruction_index < len(self.__instructions):
            # Before cycle starts:
            if command is None:
                command = self.__instructions[instruction_index][0]
                args = self.__instructions[instruction_index][1]
                if command == 'noop':
                    next_cycle = cycle + 1
                elif command == 'addx':
                    next_cycle = cycle + 2

            # During cycle:
            if part == Part.A:
                if cycle in [20, 60, 100, 140, 180, 220]:
                    signal_strength = cycle * register_x
                    total_signal_strength += signal_strength
            else:
                horz_pos_sprite = register_x % 40
                horz_pos_cursor = (cycle - 1) % 40
                if (horz_pos_sprite - 1) <= horz_pos_cursor and (horz_pos_sprite + 1) >= horz_pos_cursor:
                    # Draw at the cursor's location, if the sprite overlaps the cursor.
                    screen_buffer[cycle - 1] = True

            # After cycle ends:
            cycle = cycle + 1
            if cycle >= next_cycle:
                if command == 'noop':
                    pass
                elif command == 'addx':
                    register_x = register_x + int(args[0])
                instruction_index = instruction_index + 1
                command = None
                args = tuple()

        if part == Part.A:
            return str(total_signal_strength)
        else:
            screen = ''
            for y in range(6):
                for x in range(40):
                    screen += '#' if screen_buffer[y * 40 + x] else '.'
                screen += '\n'
            return screen

