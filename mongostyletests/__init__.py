from attest import Tests


suite = Tests()


@suite.test
def version():
    import mongostyle.version
    assert mongostyle.version.VERSION == '0.1.0'
