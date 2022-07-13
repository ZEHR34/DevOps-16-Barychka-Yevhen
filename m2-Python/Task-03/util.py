import string
from random import choice
import logging


def getRandomChar(template: str) -> str:
    k = 1
    if len(template) > 1:
        k = int(template[1:])
    elif len(template) < 1:
        return ""
    type = template[0]
    logging.debug(f'generate random chars from template: {template}')
    if type == "a":
        return "".join([choice(string.ascii_lowercase) for i in range(k)])
    elif type == "A":
        return "".join([choice(string.ascii_uppercase) for i in range(k)])
    elif type == "d":
        return "".join([choice(string.digits) for i in range(k)])
    elif type == "-":
        return "".join(["-" for i in range(k)])
    elif type == "@":
        return "".join(["@" for i in range(k)])
    else:
        logging.warning(f'unknown template: "{template}" change to _')
        return ""


def genFromTemplate(template: str) -> str:
    logging.info(f"get template: {template}")
    template = unpackTemplate(template)
    a = template.split("%")
    try:
        a.remove("")
        a.remove("")
        a.remove("")
    except ValueError:
        pass
    password = [getRandomChar(i) for i in a]
    return "".join(password)


def unpackTemplate(template: str) -> str:
    try:
        begin = template.index("[")
        end = template.index("]")
    except ValueError:
        return template
    k = 1
    if template[end+1].isnumeric():
        k = int(template[end+1])
    types = template[begin+1:end].split("%")
    types.remove("")
    newtemplete = template[:begin] + "%".join([choice(types) for _ in range(k)])+template[end+2:]
    logging.info(f"unpack template {template} to {newtemplete}")
    return newtemplete
