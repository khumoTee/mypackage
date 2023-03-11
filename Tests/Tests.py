from mypackage import MyModdule
def test_top_n():
    """
    Apply unit testing to make sure top_n works correctly
    """
    assert MyModdule.top_n([8,3,2,7,4],3)==[8,7,3], 'incorrect'