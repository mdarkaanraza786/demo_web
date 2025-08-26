import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def initFireBaseDB():
    cred = credentials.Certificate("key.json")
    firebase_admin.initialize_app(cred)

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
doc_ref=db.collection('registrationCollection').document()


def printALL():
   docs = db.collection("registrationCollection").stream()
   data = [doc.to_dict() for doc in docs]
   df = pd.DataFrame(data)
   st.dataframe(df)