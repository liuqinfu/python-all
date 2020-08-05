import configparser

parser = configparser.ConfigParser()
parser.read("./sets.ini")
sections = parser.sections()
print(sections)
options = parser.options("section1")
print(options)
items = parser.items("section1")
print(items)
phone = parser.getint("section1", "phone")
print(phone)
dicts = dict(items);
print(dicts)
