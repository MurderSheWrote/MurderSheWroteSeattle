# -*- coding: utf-8 -*-
from crimemapper.models import DBSession, Entry


def test_create_new_entry(dbtransaction, entry_dict):
    """Test new entry fixture."""
    new_entry = Entry(**entry_dict)
    assert new_entry.id is None
    DBSession.add(new_entry)
    DBSession.flush()
    assert new_entry.id is not None
