from pathlib import Path
import random
import shutil
import secrets


def move_files():
    Path("compose.yml").rename(Path("../compose.yml"))


def delete_project_dir():
    """Removes the project folder."""
    shutil.rmtree("../{{ cookiecutter._project_dir }}")


def main():
    """Final touches to our project."""
    move_files()
    delete_project_dir()


if __name__ == "__main__":
    main()
