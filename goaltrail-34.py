# === Stage 34: Add support for multiple local user profiles ===
# Project: GoalTrail
import json, os
from pathlib import Path

class ProfileManager:
    def __init__(self, data_dir=".goaltrail"):
        self.data_dir = Path(data_dir)
        self.profiles_file = self.data_dir / "profiles.json"
        self.current_profile = None
        self._ensure_profiles()

    def _ensure_profiles(self):
        if not self.profiles_file.exists():
            with open(self.profiles_file, 'w') as f:
                json.dump({"default": {"name": "Default", "goals": []}}, f)

    def load_profile(self, name=None):
        if not self.profiles_file.exists():
            return None
        try:
            with open(self.profiles_file, 'r') as f:
                profiles = json.load(f)
            if name is None or name == "default":
                profile_name = list(profiles.keys())[0]
            else:
                profile_name = name
            self.current_profile = profiles.get(profile_name, {})
            return self.current_profile
        except (json.JSONDecodeError, KeyError):
            return {}

    def save_profile(self, name=None, data=None):
        if not self.profiles_file.exists():
            with open(self.profiles_file, 'w') as f:
                json.dump({}, f)
        try:
            with open(self.profiles_file, 'r') as f:
                profiles = json.load(f)
        except (json.JSONDecodeError):
            profiles = {}
        if name is None or name == "default":
            profile_name = list(profiles.keys())[0] if profiles else "default"
        else:
            profile_name = name
        if data is not None:
            profiles[profile_name] = data
        with open(self.profiles_file, 'w') as f:
            json.dump(profiles, f, indent=2)

    def get_profile_path(self):
        return self.data_dir / f"{self.current_profile.get('name', 'default')}_goals.json" if self.current_profile else None
