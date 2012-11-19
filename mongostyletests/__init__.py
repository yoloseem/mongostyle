from attest import Tests


suite = Tests()


@suite.test
def version():
    import mongostyle
    assert mongostyle.VERSION == '0.1.0'
