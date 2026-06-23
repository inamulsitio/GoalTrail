# === Stage 16: Add argparse support for the most common commands ===
# Project: GoalTrail
import argparse

def main():
    parser = argparse.ArgumentParser(description="GoalTrail CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Goal management
    goal_parser = subparsers.add_parser('goal', help='Manage goals')
    goal_parser.set_defaults(func=cmd_goal)
    goal_add = goal_parser.add_argument('--add', '-a', nargs='+', help='Add new goals and milestones')
    goal_list = goal_parser.add_argument('--list', '-l', action='store_true', help='List all goals')
    
    # Routine management
    routine_parser = subparsers.add_parser('routine', help='Manage routines')
    routine_parser.set_defaults(func=cmd_routine)
    routine_add = routine_parser.add_argument('--add', '-a', nargs='+', help='Add new routines')
    routine_list = routine_parser.add_argument('--list', '-l', action='store_true', help='List all routines')
    
    # Blocker management
    blocker_parser = subparsers.add_parser('blocker', help='Manage blockers')
    blocker_parser.set_defaults(func=cmd_blocker)
    blocker_add = blocker_parser.add_argument('--add', '-a', nargs='+', help='Add new blockers')
    blocker_list = blocker_parser.add_argument('--list', '-l', action='store_true', help='List all blockers')
    
    # Notes management
    note_parser = subparsers.add_parser('note', help='Manage notes')
    note_parser.set_defaults(func=cmd_note)
    note_add = note_parser.add_argument('--add', '-a', nargs='+', help='Add new notes')
    note_list = note_parser.add_argument('--list', '-l', action='store_true', help='List all notes')
    
    # Reports
    report_parser = subparsers.add_parser('report', help='Generate reports')
    report_parser.set_defaults(func=cmd_report)
    report_type = report_parser.add_argument('--type', '-t', choices=['daily', 'weekly'], default='daily')
    
    args = parser.parse_args()
    if not hasattr(args, 'command'):
        parser.print_help()
        return
    args.func(**vars(args))

def cmd_goal(add=None, list=False):
    print(f"Goals: {add or []}" if add else "List goals (list flag ignored in demo)")
    if list: print("All active goals displayed.")

def cmd_routine(add=None, list=False):
    print(f"Routines: {add or []}" if add else "List routines (list flag ignored in demo)")
    if list: print("All daily routines displayed.")

def cmd_blocker(add=None, list=False):
    print(f"Blockers: {add or []}" if add else "List blockers (list flag ignored in demo)")
    if list: print("Current obstacles listed.")

def cmd_note(add=None, list=False):
    print(f"Notes: {add or []}" if add else "List notes (list flag ignored in demo)")
    if list: print("All personal notes displayed.")

def cmd_report(type='daily'):
    print(f"Generating {type} progress report...")
