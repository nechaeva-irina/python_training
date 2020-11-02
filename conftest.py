import pytest
from fixture.application import Application
#from fixture.application2 import Application2


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

#def app2(request):
  #  fixture = Application2()
   # request.addfinalizer(fixture.destroy2)
  #  return fixture

