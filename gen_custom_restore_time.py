#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://t.me/ShtabskiyAD

from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

tdate = datetime.today() - timedelta(hours=10, minutes=0)
recover_time = tdate.strftime('%Y-%m-%d %H:%M:%S')


tree = ET.parse('to_time.xml')
root = tree.getroot()

for i in root.iter('toTimeValue'):
	new_i = str(recover_time)
	i.text = str(new_i)

	for a in root.iter('timeValue'):
		new_a = str(recover_time)
		a.text = str(new_a)

tree.write('custom_to_time.xml', short_empty_elements=False, encoding='UTF-8', xml_declaration=True)
