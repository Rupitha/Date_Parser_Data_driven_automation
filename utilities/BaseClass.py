import pytest


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("getdata")
class BaseClass:
    pass
