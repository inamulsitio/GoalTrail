# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: GoalTrail
import sys


def handle_interrupt():
    """Gracefully handle Ctrl+C in CLI entry point."""
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoalTrail interrupted by user.", file=sys.stderr)
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(handle_interrupt())
