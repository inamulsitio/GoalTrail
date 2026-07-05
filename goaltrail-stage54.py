# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: GoalTrail
def colorize(text, style=""):
    codes = {"reset": "\033[0m", "bold": "\033[1m", "red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m", "blue": "\033[94m"}
    if not style: return text
    prefix = codes.get(style, "") + codes["bold"]
    suffix = codes["reset"]
    return f"{prefix}{text}{suffix}"

def print_report(goal_name, status="active", progress=0):
    print(colorize(f"[{status.upper()}] {goal_name}", "green"))
    if progress > 0:
        bar_len = int(20 * progress / 100)
        empty_bar = "-" * (20 - bar_len)
        filled_bar = "#" * bar_len
        print(f"Progress: [{filled_bar}{empty_bar}] {progress}%")
    else:
        print("Status:", status)

def log_milestone(goal_name, milestone_text):
    print(colorize(f"\n>>> Milestone achieved for '{goal_name}'", "blue"))
    print(milestone_text)
