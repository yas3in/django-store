


def valid_phone_number(value):
    if len(value) != 11:
        raise Exception("size number is not true, like this:09123456789")
    if value.startswith("09"):
        return True
    raise Exception("format invalid, correct format: 09*********")