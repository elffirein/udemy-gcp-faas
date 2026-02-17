import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
import random

# Path to your service account key file
# In a Cloud Run/Functions environment, you'd typically store this
# securely (e.g., in Secret Manager) and mount it as a file.
# For local testing, you might place it in your project directory.
SERVICE_ACCOUNT_KEY_PATH = "/tmp/serviceAccountKey.json"

# Initialize the Firebase Admin SDK with credentials from the service account key file
cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
firebase_admin.initialize_app(cred, name='udemy-gcp-faas-app')

#firebase_admin.initialize_app(name='udemy-gcp-faas-app')
# Get a Firestore client for the specific database
db = firestore.client(app=firebase_admin.get_app(name='udemy-gcp-faas-app'))

print(f"Successfully connected to Firestore database: udemy-gcp-faas")

def set_expense(request):
    from datetime import datetime
    import random
    data = {
        "expense": 100,
        "description": "This is an expense added to udemy-gcp-faas",
        "timestamp": firestore.SERVER_TIMESTAMP
    }
    try:
        ref = db.collection('expenses').document()
        print(f"collection is available")
        ref.set(data)
        print(f"Data is added")
        return 'OK', 200
    except Exception as e:
        return e, 400

