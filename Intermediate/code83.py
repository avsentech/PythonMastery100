# Code #83: Solve Tower of Hanoi
"""
    🧠 Why This Matters?
    Used in:
    - 🧩 Teaching recursion & stack-based thinking
    - 🧮 Algorithmic problem solving
    - 🕹️ Game logic & simulations
    - 🧠 Cognitive training apps and academic modules
"""
# Tier: Intermediate
# Goal: Move all disks from source to target using an auxilary peg, following these rules:
"""
    - Only one disk can be moved at a time.
    - A disk cannot be placed on top of a smaller one.
    - Only topmost disk from any peg can be moved.   
"""

# Python Code
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

# Sample Usage
disks = 3
tower_of_hanoi(disks, "A", "C", "B")

# Sample Output
"""
    Move disk 1 from A to C
    Move disk 2 from A to B
    Move disk 1 from C to B
    Move disk 3 from A to C
    Move disk 1 from B to A
    Move disk 2 from B to C
    Move disk 1 from A to C
"""

# Concept Breakdown
"""
    Concept             Description
    --------------------------------
    Recursive Divide    Break problem into subproblems (n-1 disks)
    Base Case           Move single disk directly
    Order Matters       Recursion builds move order precisely
    Pegs                Abstract labels for source/target/auxiliary
"""
# Minimum number of moves: 2^n-1 For n = 3, moves = 7

# Real-World Connection
"""
    - Teaching recursion through visual metaphors
    - Building logic in puzzle games
    - Modeling robotic movement with constraints
    - Taks scheduling and stack simulation in systems
"""