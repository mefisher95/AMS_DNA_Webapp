from subprocess import run
from sys import argv


def ship() -> None:
    run('git add ./../.', shell=True)
    run('git commit -m "quick push"', shell=True)
    run('git push', shell=True)


if __name__ == "__main__":
    if argv[1] == "ship": ship()
    # elif argv[1] == "delpoy": ship()