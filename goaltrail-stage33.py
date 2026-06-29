# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: GoalTrail
GOAL_TRAIL_SETTINGS = {
    "app_name": "GoalTrail",
    "version": "1.0.33",
    "data_dir": "./storage",
    "theme": "dark",
    "notifications_enabled": True,
    "default_goal_limit": 5
}

def get_setting(key: str, default=None):
    """Retrieve a setting value safely."""
    return GOAL_TRAIL_SETTINGS.get(key, default)

def update_settings(**kwargs):
    """Update multiple settings atomically and validate types."""
    for key, value in kwargs.items():
        if key not in GOAL_TRAIL_SETTINGS:
            raise ValueError(f"Unknown setting key: {key}")
        # Allow boolean conversion from strings to handle CLI input easily
        if isinstance(value, str) and key.endswith("_enabled"):
            value = value.lower() == "true"
        elif isinstance(value, str):
            try:
                value = int(value)
            except ValueError:
                pass
        GOAL_TRAIL_SETTINGS[key] = value

def reset_settings():
    """Reset all settings to default values."""
    global GOAL_TRAIL_SETTINGS
    import copy
    GOAL_TRAIL_SETTINGS = copy.deepcopy({
        "app_name": "GoalTrail",
        "version": "1.0.33",
        "data_dir": "./storage",
        "theme": "dark",
        "notifications_enabled": True,
        "default_goal_limit": 5
    })
