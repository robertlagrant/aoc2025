from collections import deque

from day1 import inputs

dial = deque(range(100))
dial.rotate(50)

zeroes_at_stop_count = 0
zeroes_in_passing_count = 0

for rotation in inputs.rotations.splitlines():
    direction = -1 if rotation[0] == "L" else 1
    number = int(rotation[1:])

    for _ in range(number):
        dial.rotate(direction)

        if dial[0] == 0:
            zeroes_in_passing_count += 1

    if dial[0] == 0:
        zeroes_at_stop_count += 1

print(f"Part 1: {zeroes_at_stop_count}")
print(f"Part 2: {zeroes_in_passing_count}")
