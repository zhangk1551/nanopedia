from absl import app
from absl import flags
import csv
import pandas as pd

FLAGS = flags.FLAGS
flags.DEFINE_string('key', 'Year', 'Key to sort.')
flags.DEFINE_bool('save', False, 'Whether save the new data to original path.')
flags.DEFINE_bool('update_countries', False,
                  'Whether update the country data to country.csv.')
flags.DEFINE_bool('update_categories', False, 
                  'Whether update the category data to category.csv.')

COLUMN_NAMES = ['Year', 'Country', 'Description', 'People', 'Category']
EVENTS_DATA_PATH = "data/historical_events.csv"
COUNTRY_DATA_PATH = "data/country.csv"
CATEGORY_DATA_PATH = "data/category.csv"
 
def main(argv):
  if FLAGS.key not in COLUMN_NAMES:
    print("Invalid key.")
    return
  historical_events = pd.read_csv(EVENTS_DATA_PATH, names=COLUMN_NAMES,
  index_col=False, quoting=csv.QUOTE_NONE).sort_values(FLAGS.key).reset_index(drop=True)
  print(historical_events)
  if FLAGS.save:
    historical_events.to_csv(EVENTS_DATA_PATH, header=False,
    index=False,quoting=csv.QUOTE_NONE)
  if FLAGS.update_countries:
    historical_events['Country'].value_counts().to_csv(COUNTRY_DATA_PATH,
    header=False)
  if FLAGS.update_categories:
    historical_events['Category'].value_counts().to_csv(CATEGORY_DATA_PATH,
    header=False)

if __name__ == '__main__':
  app.run(main)
