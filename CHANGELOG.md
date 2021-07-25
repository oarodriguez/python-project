# Changelog

Versions follow [CalVer](https://calver.org).

## 21.1.1 (Not yet released)

### Added

- Add a GitHub action to run the tests on every push to the main branch.
- Enable support to run code quality checks using the `pre-commit` library.
- Add development tasks to install, uninstall, and upgrade the project package.

### Changed

- In the package entry file, `src/pyproject/__init__.py`, the `__name__`
  variable must match the name set in the `tool.poetry` section of the
  `pyproject.toml` file.
- Use `click` to create the command line interfaces for development tasks.

### Deprecated

TODO.

### Removed

- Remove redundant development tasks.

### Fixed

TODO.

## 21.1.0 (2021-07-24)

### Added

- Define the project structure and fundamental elements.
