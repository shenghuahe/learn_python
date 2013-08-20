try:
    None.call_some_method()
except Exception as ex:
    print ex.args[0]