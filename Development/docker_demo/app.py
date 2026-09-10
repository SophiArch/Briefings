import platform

import pyfiglet


def main():
    banner = pyfiglet.figlet_format("Hello Docker")
    print(banner)
    print(f"Python version : {platform.python_version()}")
    print(f"Platform       : {platform.system()} ({platform.machine()})")
    print("Running inside a container — no host installs required!")


if __name__ == "__main__":
    main()
