from absl import app
from absl import flags
import pandas as pd

FLAGS = flags.FLAGS
flags.DEFINE_string('key', 'Year', 'Key to sort.')

def main(argv):
  path = "data/historical_events.csv"
  column_names = ['Year', 'Country', 'Description', 'People', 'Category']
  if key not in column_names:
    print("Invalid key.")
    return
  historical_events = pd.read_csv(path, names=column_names,
  index_col=False).sort_values(FLAGS.key).reset_index(drop=True)
  print(historical_events)

if __name__ == '__main__':
  app.run(main)
