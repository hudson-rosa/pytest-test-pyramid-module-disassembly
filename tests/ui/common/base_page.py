from pathlib import Path


class BasePage:

    @staticmethod
    def get_dashboard_path() -> Path:
        project_root = Path(__file__).resolve().parents[3]
        return project_root / "artifacts" / "calangobotics_dashboard.html"
