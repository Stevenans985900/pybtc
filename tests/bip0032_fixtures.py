import pytest


@pytest.fixture
def fail_key1():
    return b'\x00\x00\x00\x00'


@pytest.fixture
def fail_key2():
    return b'\x97\x8bq\xc6\xd8\xfew\xe5\xfa\xad\xdc\xc6\xc5\x91\xbd\xfb'


@pytest.fixture
def good_key():
    return b'B\xa8\xe9v>y\xe2\x82\x10\x80\xc2\xa91\x10E\xe0XJ\xe6\xc7\x18\x9eE~\xa0^\xd1\x820\xe7\x18\x0c'

@pytest.fixture
def master_key_hdwallet():
    return dict(version=b'\x04\x88\xad\xe4',
                key=b"Y\x9e'\xe00or'\xacD\x9c(l\x99\x0fxB\x03\xbd/]|+\xfd\xe89K!\x93\x0bN\x9b",
                depth=0,
                child=0,
                finger_print=b'\x00\x00\x00\x00',
                chain_code=b'B\xa8\xe9v>y\xe2\x82\x10\x80\xc2\xa91\x10E\xe0XJ\xe6\xc7\x18\x9eE~\xa0^\xd1\x820\xe7\x18\x0c',
                is_private=True)


@pytest.fixture
def public_key_hdwallet():
    return dict(version=b'\x04\x88\xB2\x1E',
                key=b"Y\x9e'\xe00or'\xacD\x9c(l\x99\x0fxB\x03\xbd/]|+\xfd\xe89K!\x93\x0bN\x9b",
                depth=0,
                child=0,
                finger_print=b'\x00\x00\x00\x00',
                chain_code=b'B\xa8\xe9v>y\xe2\x82\x10\x80\xc2\xa91\x10E\xe0XJ\xe6\xc7\x18\x9eE~\xa0^\xd1\x820\xe7\x18\x0c',
                is_private=False)
