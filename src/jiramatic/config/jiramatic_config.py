"""Jiramatic project configuration."""

from loguru import logger as lg

from jiramatic.config.jiramatic_paths import JiramaticPaths
from jiramatic.config.singleton import Singleton


class JiramaticConfig(metaclass=Singleton):
    """Jiramatic project configuration."""

    def __init__(self) -> None:
        lg.info(f"Loading Jiramatic config")
        self.paths = JiramaticPaths()

    def __str__(self) -> str:
        s = "JiramaticConfig:"
        s += f"\n{self.paths}"
        return s

    def __repr__(self) -> str:
        return str(self)


def get_jiramatic_config() -> JiramaticConfig:
    """Get the jiramatic config."""
    return JiramaticConfig()


def get_jiramatic_paths() -> JiramaticPaths:
    """Get the jiramatic paths."""
    return get_jiramatic_config().paths
