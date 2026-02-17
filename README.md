# udemy-gcp-faas
Test checkin

gcloud secrets create service-account-key-secret --data-file=/d/Kaustuv/GCP_DevOps/udemy_fass_cloudfunc/udemy-gcp-faas/venv/google-credentials.json

gcloud secrets add-iam-policy-binding service-account-key-secret \
    --role="roles/secretmanager.secretAccessor" \
    --member="serviceAccount:firebase-adminsdk-fbsvc@udemy-gcp-faas.iam.gserviceaccount.com"

gcloud functions deploy set_expense \
  --runtime python310 \
  --trigger-http \
  --set-secrets /tmp/serviceAccountKey.json=service-account-key-secret:latest \
  --allow-unauthenticated

