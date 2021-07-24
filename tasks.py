"""
Collection of development tasks.

Usage:
    python -m tasks TASK-NAME
"""
import shutil
from enum import Enum, unique
from pathlib import Path
from subprocess import run
from typing import List

import click

from pyproject import __version__

PROJECT_DIR = Path(__file__).parent
SRC_DIR = PROJECT_DIR / "src"
TESTS_DIR = PROJECT_DIR / "tests"
DOCS_DIR = PROJECT_DIR / "docs"
DOCS_SOURCE_DIR = DOCS_DIR / "source"
DOCS_BUILD_DIR = DOCS_DIR / "build"
NOTEBOOKS_DIR = PROJECT_DIR / "notebooks"
TASKS_FILE = PROJECT_DIR / "tasks.py"

ISORT_CMD = "isort"
BLACK_CMD = "black"
PYDOCSTYLE_CMD = "pydocstyle"
FLAKE8_CMD = "flake8"
MYPY_CMD = "mypy"
PYTEST_CMD = "pytest"
SPHINX_BUILD_CMD = "sphinx-build"

# Coverage report XML file.
COVERAGE_XML = "coverage.xml"

# Arguments to pass to subprocess.run for each task.
BUILD_DOCS_ARGS = [
    SPHINX_BUILD_CMD,
    str(DOCS_SOURCE_DIR),
    str(DOCS_BUILD_DIR),
]
FORMAT_ARGS = [
    BLACK_CMD,
    str(TASKS_FILE),
    str(SRC_DIR),
    str(TESTS_DIR),
    str(DOCS_DIR),
    str(NOTEBOOKS_DIR),
]
ISORT_ARGS = [
    ISORT_CMD,
    str(TASKS_FILE),
    str(SRC_DIR),
    str(TESTS_DIR),
    str(NOTEBOOKS_DIR),
]
PYDOCSTYLE_ARGS = [
    PYDOCSTYLE_CMD,
    str(TASKS_FILE),
    str(SRC_DIR),
    str(TESTS_DIR),
    # str(NOTEBOOKS_DIR),
]
FLAKE8_ARGS = [
    FLAKE8_CMD,
    str(TASKS_FILE),
    str(SRC_DIR),
    str(TESTS_DIR),
    "--statistics",
]
PYTEST_ARGS = [
    PYTEST_CMD,
    "--cov",
    "--cov-report",
    "term-missing",
    "--cov-report",
    f"xml:./{COVERAGE_XML}",
]
MYPY_ARGS = [
    MYPY_CMD,
    str(TASKS_FILE),
    str(SRC_DIR),
]


def _run(command: List[str]):
    """Run a subcommand through python subprocess.run routine."""
    # NOTE: See https://stackoverflow.com/a/32799942 in case we want to
    #  remove shell=True.
    run(command)


app = click.Group("tasks")


@app.command()
def black():
    """Format the source code using black."""
    _run(FORMAT_ARGS)


@app.command()
def isort():
    """Format imports using isort."""
    _run(ISORT_ARGS)


@app.command()
def pydocstyle():
    """Run pydocstyle."""
    _run(PYDOCSTYLE_ARGS)


@app.command()
def flake8():
    """Run flake8 linter."""
    _run(FLAKE8_ARGS)


@app.command()
def mypy():
    """Run mypy."""
    _run(MYPY_ARGS)


@app.command()
def tests():
    """Run test suite."""
    _run(PYTEST_ARGS)


@app.command()
def version():
    """Project version."""
    print(__version__)


@app.command(name="format")
def format_():
    """Run all formatting tasks."""
    _run(FORMAT_ARGS)
    _run(ISORT_ARGS)


@app.command()
def typecheck():
    """Run all typechecking tasks."""
    _run(MYPY_ARGS)


@app.command()
def lint():
    """Run all linting tasks."""
    _run(PYDOCSTYLE_ARGS)
    _run(FLAKE8_ARGS)


@unique
class DocFormat(str, Enum):
    """Document Formats."""

    HTML = "html"


# Set HTML as the default document format.
default_doc_format = DocFormat.HTML.name

# List of allowed document formats.
doc_formats = list(DocFormat.__members__.keys())


@app.command()
@click.option(
    "--doc-format",
    type=click.Choice(doc_formats),
    default=default_doc_format,
    help=f"Generated documentation format. Defaults to {default_doc_format}.",
)
def build_docs(doc_format: str):
    """Build the documentation."""
    doc_format_ = DocFormat[doc_format]
    BUILD_DOCS_ARGS.extend(["-b", doc_format_])
    _run(BUILD_DOCS_ARGS)


@unique
class CleaningTask(str, Enum):
    """Cleaning tasks."""

    DOCS = "docs"


# Set DOCS as the default cleaning task.
default_cleaning_task = CleaningTask.DOCS.name

# List of allowed cleaning tasks.
cleaning_tasks = list(CleaningTask.__members__.keys())


@app.command()
@click.option(
    "--task",
    type=click.Choice(cleaning_tasks),
    default=default_cleaning_task,
    help=f"Cleaning task to perform. Defaults to {default_cleaning_task}.",
)
def clean(task: str):
    """Clean any existing documentation."""
    task_ = None if task is None else CleaningTask[task]
    if task_ is None or task_ is CleaningTask.DOCS:
        shutil.rmtree(DOCS_BUILD_DIR, ignore_errors=True)


if __name__ == "__main__":
    app()
