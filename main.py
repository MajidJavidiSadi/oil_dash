import pathlib
import pickle
from itertools import islice

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()
pickle_file_path = 'data/example.pkl'
points = pickle.load(open(DATA_PATH.joinpath("points.pkl"), "rb"))
points = dict(islice(points.items(), 200))
# Create and write the dictionary to the pickle file
with open(pickle_file_path, 'wb') as file:
    pickle.dump(points, file)

print(f'Pickle file "{pickle_file_path}" created successfully.')