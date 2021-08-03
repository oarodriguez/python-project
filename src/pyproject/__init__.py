"""pyproject - A template for your Python project.

Copyright © 2021, Omar Abel Rodríguez-López.
"""

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:  # pragma: no cover
    import importlib_metadata  # type: ignore

_metadata = importlib_metadata.metadata(__name__)  # type: ignore

# Export package information.
__version__ = _metadata["version"]
__author__ = _metadata["author"]
__description__ = _metadata["description"]
__license__ = _metadata["license"]

__all__ = ["__version__", "__author__", "__description__", "__license__"]
