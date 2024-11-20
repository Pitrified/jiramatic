"""Test the jiramatic paths."""

import pytest

from jiramatic.config.jiramatic_config import get_jiramatic_paths


def test_jiramatic_paths() -> None:
    """Test the jiramatic paths."""
    jiramatic_paths = get_jiramatic_paths()
    assert jiramatic_paths.src_fol.name == "jiramatic"
    assert jiramatic_paths.root_fol.name == "jiramatic"
    assert jiramatic_paths.data_fol.name == "data"
