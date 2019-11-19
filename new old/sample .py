# import xml.etree.ElementTree as ET
#
# data = '''<?xml version="1.0" encoding="UTF-8"?>
# <Hotel>
# <food>
#     <item name="breakfast">Idly</item>
#     <price>$2.5</price>
#     <description>   Two idly's with chutney   </description>
#     <calories>553</calories>
# </food>
# </Hotel>
# '''
# myroot = ET.fromstring(data)
# print(myroot)

'''

for description in myroot.iter('description'):
    new_desc = str(description.text) + 'wil be served'
    description.text = str(new_desc)
    description.set('updated', 'yes')

mytree.write('new.xml');

for nayn in myroot.iter('Naynesh'):
    new_desc = str(nayn.text) + 'wil be served'
    nayn.text = str(new_desc)
    # DESC.set('updated', 'yes')

mytree.write('new_Data.xml');

ET.SubElement(myroot[0], 'speciality')
for x in myroot.iter('speciality'):
    new_desc = 'South Indian Special'
    x.text = str(new_desc)

mytree.write('output5.xml')

'''
