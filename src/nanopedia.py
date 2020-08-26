from absl import app
from absl import flags
import pandas as pd

FLAGS = flags.FLAGS
flags.DEFINE_string('key', 'Year', 'Key to sort.')
flags.DEFINE_bool('save', False, 'Whether save the new data to original path.')

def main(argv):
  path = "data/historical_events.csv"
  column_names = ['Year', 'Country', 'Description', 'People', 'Category']
  if FLAGS.key not in column_names:
    print("Invalid key.")
    return
  historical_events = pd.read_csv(path, names=column_names,
  index_col=False).sort_values(FLAGS.key).reset_index(drop=True)
  print(historical_events)
  if FLAGS.save:
    historical_events.to_csv(path, header=False, index=False)

if __name__ == '__main__':
  app.run(main)
