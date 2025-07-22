# Code #98: Create a Simple Stopwatch Using time
# Tier: Intermediate
# Goal: Start, stop and measure elapsed time in seconds

# Python Code
import time

def stopwatch():
    input("⏱️ Press Enter to start the stopwatch...")
    start_time = time.time()

    input("⏹️ Press Enter to stop the stopwatch...")
    end_time = time.time()

    elapsed_time = end_time = start_time
    print(f"⏳ Elapsed time: {elapsed_time:.2f} seconds")

# Sample Usage

stopwatch()

# Sample Run
"""
⏱️ Press Enter to start the stopwatch...
⏹️ Press Enter to stop the stopwatch...
⏳ Elapsed time: 6.21 seconds
"""

# Concept Breakdown
"""
    Concept             Description
    -------------------------------
    time.time()         Captures current time in seconds (Unix time)
    elapsed_time        Difference between stop and start timestamps
    input()             User-triggered start/stop flow

    You can expand this with 
    - Multiple laps ⏱️
    - Live display updates 🔄
    - Keyboard controls 
"""

# Real-World Connection
"""
    - 🧪 Benchmarking code execution time
    - 💡 Tracking productivity bursts or Pomodoro cycles
    - 🧠 Profiling function performance manually
    - 🎮 Game timers or puzzle challenge
"""