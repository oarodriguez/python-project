# Changelog

Versions follow [CalVer](https://calver.org).

## 2021.2.0 (2021-08-19)

### Added

- Add `rope` library for development purposes.
- Add documentation source code using `sphinx` and `sphinx_rtd_theme`.
- Add a GitHub action to run the tests on every push to the main branch.
- Enable support to run code quality checks using the `pre-commit` library.
- Add development tasks to install, uninstall, and upgrade the project package.

### Changed

- Do not force the project package name to be the same as the project name in
  the `src/pyproject/__init__.py`. We must recover the package metadata
  stating the project name in the code.
- Make the package metadata a public name of the project package.
- Use `click` to create the command line interfaces for development tasks.

### Removed

- Remove redundant development tasks.

### Fixed

- Fix tasks to install, uninstall, and upgrade the project package.

---

## 21.1.0 (2021-07-24)

### Added

- Define the project structure and fundamental elements.
