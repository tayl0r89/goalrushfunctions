from google.cloud import firestore
import pandas as pd

db = firestore.Client()

results = db.collection("results").where("Div", "==", "E0").stream()

data = []
for result in results:
    data.append(result.to_dict())

print(pd.DataFrame(data))