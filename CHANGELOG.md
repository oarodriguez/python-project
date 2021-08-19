# Changelog

Versions follow [CalVer](https://calver.org).

## 21.1.1 (Not yet released)

### Added

- Add `rope` library for development purposes.
- Add documentation source code using `sphinx` and `sphinx_rtd_theme`.
- Add a GitHub action to run the tests on every push to the main branch.
- Enable support to run code quality checks using the `pre-commit` library.
- Add development tasks to install, uninstall, and upgrade the project package.

### Changed

- Make the package metadata a public name of the project package.
- In the package entry file, `src/pyproject/__init__.py`, the `__name__`
  variable must match the name set in the `tool.poetry` section of the
  `pyproject.toml` file.
- Use `click` to create the command line interfaces for development tasks.

### Deprecated

TODO.

### Removed

- Remove redundant development tasks.

### Fixed

- Fix tasks to install, uninstall, and upgrade the project package.

---

## 21.1.0 (2021-07-24)

### Added

- Define the project structure and fundamental elements.
