# -*- coding: utf-8 -*-
"""
Tower of Hanoi Program

You are given:

Three rods: Let's call them A (source), B (auxiliary), and C (target).

N disks: All are of different sizes and initially placed on rod A in decreasing order of size, with the largest at the bottom and the smallest at the top.

Move all the disks from rod A to rod C (target), following these three rules:

Only one disk can be moved at a time.
You can only move the top disk of any rod.
A larger disk can never be placed on top of a smaller disk.

"""

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Example usage:
n = int(input("Enter n - no of disks"))  # number of disks
tower_of_hanoi(n, 'Src', 'Target', 'Aux')

