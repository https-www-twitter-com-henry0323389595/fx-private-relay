"""Shared fixtures for privaterelay tests"""

import json
from collections.abc import Iterator
from pathlib import Path

import pytest
from pytest_django.fixtures import SettingsWrapper

from privaterelay.utils import get_version_info


@pytest.fixture
def version_json_path(tmp_path: Path, settings: SettingsWrapper) -> Iterator[Path]:
    """Create testing version.json file, cleanup after test."""
    get_version_info.cache_clear()
    settings.BASE_DIR = tmp_path
    path = settings.BASE_DIR / "version.json"
    default_build_info = {
        "commit": "the_commit_hash",
        "version": "2024.01.17",
        "source": "https://github.com/mozilla/fx-private-relay",
        "build": "https://circleci.com/gh/mozilla/fx-private-relay/100",
    }
    path.write_text(json.dumps(default_build_info))
    yield path
    get_version_info.cache_clear()
