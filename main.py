import pandas as pd
from catboost import CatBoostRegressor
# Initialize data

train_data = [[1, 4, 5, 6],
              [4, 5, 6, 7],
              [30, 40, 50, 60]]

eval_data = [[2, 4, 6, 8],
             [1, 4, 50, 60]]

train_labels = [10, 20, 30]
# Initialize CatBoostRegressor
model = CatBoostRegressor(iterations=2,
                          learning_rate=1,
                          depth=2)
# Fit model
model.fit(train_data, train_labels)
# Get predictions
preds = model.predict(eval_data)

# Convert predictions to DataFrame and write to TSV
preds_df = pd.DataFrame(preds)
out_file = 'predictions.tsv'

preds_df.to_csv(out_file, sep='\t', index=False)

print("Script finished!")
