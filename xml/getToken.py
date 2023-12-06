import jxmlease

tokenfile = './token.xml'

with open(tokenfile, 'r') as file:
    xml_content = file.read()

parsed_xml = jxmlease.parse(xml_content)



tokenfinded = parsed_xml['soap-env:Envelope']['soap-env:Header']['wsse:Security']['wsse:BinarySecurityToken']

print("token:", tokenfinded)
