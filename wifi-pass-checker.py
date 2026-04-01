import subprocess
from typing import List, Dict


class WifiManager:
    """Handles Wi-Fi profile operations using netsh."""

    @staticmethod
    def _run_command(command: List[str]) -> str:
        """Executes a system command and returns output."""
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.output or ""

    def get_profiles(self) -> List[str]:
        """Fetch all saved Wi-Fi profiles."""
        output = self._run_command(["netsh", "wlan", "show", "profiles"])
        profiles = []

        for line in output.split("\n"):
            if "All User Profile" in line:
                profiles.append(line.split(":")[1].strip())

        return profiles

    def get_profile_details(self, profile: str) -> Dict[str, str]:
        """Fetch details (including password) for a given profile."""
        output = self._run_command(
            ["netsh", "wlan", "show", "profile", profile, "key=clear"]
        )

        details = {
            "name": profile,
            "password": None
        }

        for line in output.split("\n"):
            if "Key Content" in line:
                details["password"] = line.split(":")[1].strip()

        return details

    def get_all_profiles_with_passwords(self) -> List[Dict[str, str]]:
        """Get all Wi-Fi profiles with passwords."""
        profiles = self.get_profiles()
        return [self.get_profile_details(p) for p in profiles]


def print_profiles(profiles: List[Dict[str, str]]) -> None:
    """Nicely print Wi-Fi profiles."""
    print("=" * 40)
    print(" Saved Wi-Fi Profiles ")
    print("=" * 40)

    for profile in profiles:
        print(f"SSID     : {profile['name']}")
        print(f"Password : {profile['password'] or 'N/A'}")
        print("-" * 40)


def main():
    wifi_manager = WifiManager()
    profiles = wifi_manager.get_all_profiles_with_passwords()
    print_profiles(profiles)


if __name__ == "__main__":
    main()