import pandas as pd
import os
import utils

actual_data_path = os.path.join(utils.BASE_PATH, 'result/gender_submission.csv')
trained_data_path = os.path.join(utils.BASE_PATH, 'result/titanic_submission.csv')
actual_data = pd.read_csv(actual_data_path)
trained_data = pd.read_csv(trained_data_path)

last_data = pd.merge(actual_data, trained_data, on='PassengerId',validate="one_to_one")
count = 0
for ix, row in last_data.iterrows():
    if row[1] == row[2]:
        count += 1
    else:
        pass
total_count = len(last_data)
accuracy_rate = float(count) / float(total_count)
print(accuracy_rate)
