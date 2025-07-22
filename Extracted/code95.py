# Code #05: Create a Countdown Timer Using time
"""
    🧠 Why This Matters?
    Used in:
    - 🚀 CLI productivity timers
    - ⏱️ Session or task timing apps
    - 🧪 Delay simulations for testing
    - 🔔 Notification systems & reminder
"""
# Tier: Beginner-to-Intermediate
# Goal: Countdown from a given number of seconds

# Python Code
import time
def countdown(seconds):
    print(f"⏳ Starting countdown: {seconds} seconds\n")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(f"🕒 {timer_display}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\n🚀 Countdown complete!")

# Sample usage
countdown(10)