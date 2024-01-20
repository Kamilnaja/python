import pandas as pd

# Your date string
date_string = '2023-10-10'

# Convert the date string to a Pandas datetime object
date_object = pd.to_datetime(date_string)

# Convert the datetime object to milliseconds
milliseconds = date_object.timestamp() * 1000

print(milliseconds)
