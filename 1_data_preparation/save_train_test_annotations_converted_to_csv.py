import pandas as pd

# definim functia de codificare a etichetelor
def label_encoding(x):
    labels = {'person': 0, 
              'car': 1, 
              'chair': 2, 
              'bottle': 3, 
              'pottedplant': 4, 
              'bird': 5, 
              'dog': 6,
              'sofa': 7, 
              'bicycle': 8, 
              'horse': 9, 
              'boat': 10, 
              'motorbike': 11, 
              'cat': 12, 
              'tvmonitor': 13,
              'cow': 14, 
              'sheep': 15, 
              'aeroplane': 16, 
              'train': 17, 
              'diningtable': 18, 
              'bus': 19}
    return labels[x]

# citim fisierele CSV
train_data = pd.read_csv('D:\\Facultate\\0.Proiect licenta\\1_data_preparation\\train_annotations.csv')
test_data = pd.read_csv('D:\\Facultate\\0.Proiect licenta\\1_data_preparation\\test_annotations.csv')

# aplicam functia de codificare a etichetelor pe coloana name
train_data['name'] = train_data['name'].apply(label_encoding)
test_data['name'] = test_data['name'].apply(label_encoding)

pd.set_option('display.max_rows', None)

# salvam in fisiere CSV
train_data.to_csv('train_annotations_converted.csv', index = False)
test_data.to_csv('test_annotations_converted.csv', index = False)

pd.reset_option('display.max_rows')
