import xml.etree.ElementTree as ET

mytree = ET.parse('Myxml.xml')
myroot = mytree.getroot()
# print(myroot)

print(myroot.tag)
print(myroot.tag[0:4])
print(myroot.attrib)
print(myroot[0].tag)
print("__" * 25)

for x in myroot[0]:
    print(x.text)
print("__" * 25)

for x in myroot.findall('food'):
    item = x.find('item').text
    price = x.find('price').text
    desc = x.find('description').text

    print(item, price, desc)

    ET.SubElement(x, 'speciality')

    for j in myroot.iter('speciality'):
        new_desc = 'South Indian Special'
        j.text = str(new_desc)

print("__" * 25)
mytree.write('Myxml.xml')
