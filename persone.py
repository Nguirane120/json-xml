import jxmlease

parser = jxmlease.Parser()

xm_file = './persone.xml'

with open(xm_file, "r") as file:
    xml_content = file.read()
    # print(xml_content)


parse_data = parser(xml_content) 

getPersonne = parse_data['root']['person']

for p in getPersonne:
    print(f"{p['name']} a {p['age']} ans ")