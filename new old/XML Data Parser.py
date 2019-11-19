import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

# all items data
print('Expertise Data:')
print('Rank \tYear\t\tGDPPC')

for elem in root:
    for subelem in elem:
        print(subelem.text, end="\t\t")
    print("")
