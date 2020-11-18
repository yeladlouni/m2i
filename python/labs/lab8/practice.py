import xml.etree.ElementTree as ET

tree = ET.parse('countries.xml')

root = tree.getroot()

for country in root:
    for child in list(country):
        print(child.tag, child.text)
        for attribute in child.attrib:
            print(attribute, child.attrib[attribute])
