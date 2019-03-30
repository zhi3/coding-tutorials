from mypkg import app

def test_app():
    obj = app.App(1)
    assert obj.getV() == 1

