# -*- coding: utf-8 -*-
"""Test that initializedb runs when called. Tests to boost coverage."""
import pytest
from crimemapper.scripts.initializedb import main


def test_main(config_path, test_url):
    """Test that main in intializedb runs when called with correct args."""
    main(['initialize_db',
          config_path])


def test_main_error():
    """Test that main doesn't run without an dev.ini file."""
    with pytest.raises(SystemExit):
        main(['initialize_db'])
