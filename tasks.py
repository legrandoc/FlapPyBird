# pylint: skip-file
from invoke import task


@task
def run(c):
    """Run the game"""
    c.run("python main.py")


@task
def web(c):
    """Run the web server"""
    c.run("pygbag main.py")


@task
def web_build(c):
    """Build for web"""
    c.run("pygbag --build main.py")


@task
def init(c):
    """Initialize the project"""
    c.run("pip install -U pip")
    c.run('pip install -e ".[dev]"')
    c.run("pre-commit install")


@task
def format(c):
    """Format the code"""
    c.run("black .")


@task
def lint(c):
    """Run linting"""
    c.run(
        "flake8 --config=../.flake8 --output-file=./coverage/flake8-report --format=default"
    )


@task
def pre_commit(c):
    """Install pre-commit hooks"""
    c.run("pre-commit install")


@task
def pre_commit_all(c):
    """Run pre-commit on all files"""
    c.run("pre-commit run --all-files")
