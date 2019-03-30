from mypkg import view

def testView():
    obj = view.View(1)
    assert obj.getV() == 1