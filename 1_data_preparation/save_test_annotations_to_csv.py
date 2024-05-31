import os
import pandas as pd
from xml.etree import ElementTree as et

# folderul care contine imaginile de testare
test_image_folder = r'D:\Facultate\0.Proiect licenta\1_data_preparation\data_images\test'

# folderul care contine fisierele XML
xml_dir = r'D:\Facultate\0.Proiect licenta\1_data_preparation\data_images\annotations'

# listele pentru a stoca numele fisierelor XML pentru imaginile de testare si informatiile corespunzatoare
xml_files_test = []
xml_data_test = []

# extragem numele imaginilor de testare din folder
test_images = os.listdir(test_image_folder)

# parcurgem fiecare fisier XML din folderul annotations
for xml_file in os.listdir(xml_dir):
    # verificam daca fisierul XML corespunde unei imagini de testare
    if xml_file.replace('.xml', '.jpg') in test_images:
        xml_path = os.path.join(xml_dir, xml_file)

        # extragem informatiile din fisierul XML
        tree = et.parse(xml_path)
        root = tree.getroot()
        image_name = root.find('filename').text
        width = root.find('size').find('width').text
        height = root.find('size').find('height').text
        objs = root.findall('object')

        for obj in objs:
            name = obj.find('name').text
            bndbox = obj.find('bndbox')
            xmin = bndbox.find('xmin').text
            xmax = bndbox.find('xmax').text
            ymin = bndbox.find('ymin').text
            ymax = bndbox.find('ymax').text

            xml_data_test.append([image_name, width, height, name, xmin, xmax, ymin, ymax])

        xml_files_test.append(xml_file)

# convertim lista cu date intr-un dataframe
df_test = pd.DataFrame(xml_data_test, columns = ['filename', 'width', 'height', 'name', 'xmin', 'xmax', 'ymin', 'ymax'])

# salvam dataframe-ul intr-un fisier CSV
df_test.to_csv('test_annotations.csv', index = False)
