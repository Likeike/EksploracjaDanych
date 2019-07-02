from TextManipulator import *

import pandas as pd

text_manipulator = TextManipulator()

# ładowanie pliku csv
data_frame = pd.read_csv('csv/drugsComTest_raw_test.csv', usecols=['drugName', 'review', 'rating'])

# obrabianie tekstu
data_frame['review_replaced'] = data_frame.apply(lambda row: text_manipulator.manipulate(row['review']), axis=1)

# obliczanie good & bad
data_frame['review_result'] = data_frame.apply(lambda row: text_manipulator.count_result(row['review_replaced']), axis=1)

print(data_frame.tail())

