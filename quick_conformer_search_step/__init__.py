# -*- coding: utf-8 -*-

"""
quick_conformer_search_step
A SEAMM plug-in for a simple, quick conformer search
"""

# Bring up the classes so that they appear to be directly in
# the quick_conformer_search_step package.

from .quick_conformer_search import QuickConformerSearch  # noqa: F401, E501
from .quick_conformer_search_parameters import QuickConformerSearchParameters  # noqa: F401, E501
from .quick_conformer_search_step import QuickConformerSearchStep  # noqa: F401, E501
from .tk_quick_conformer_search import TkQuickConformerSearch  # noqa: F401, E501

from .metadata import metadata  # noqa: F401

# Handle versioneer
from ._version import get_versions

__author__ = "Paul Saxe"
__email__ = "psaxe@molssi.org"
versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
