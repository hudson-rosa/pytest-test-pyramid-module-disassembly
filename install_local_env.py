import os

def main():
    run_updates()


def run_updates():
    _v3 = set_for_unix()

    print("\nUpdating PIP...")
    
    os.system(f"rm -rf .venv venv")
    os.system(f"python{_v3} -m venv venv")
    os.system(f"source venv/bin/activate")

    print("\nUpdating all packages and resources...")
    os.system(f"pip install -r requirements.txt")
    os.system(f"pip install playwright")
    os.system(f"playwright install --with-deps")
    os.system(f"pip install --upgrade pip")

    print("\nPackages installed:")
    os.system(f"which python")
    os.system(f"which pip")
    os.system(f"pip list")


def set_for_unix():
    if os.name != "nt":
        return "3"


class Update:
    if __name__ == "__main__":
        main()
