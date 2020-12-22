`gcloud auth login`

`gcloud condif set project PROJECT_ID`

`gcloud functions deploy search_fii_reports --trigger-topic search-fii-reports --runtime python37`

# Testando

`gcloud functions call search_fii_reports --data '{"topic":"search-fii-reports","message":"Hello World!", "data": ["ABCP11"]}'`


# ver logs

`gcloud functions logs read search_fii_report`

# Referências

- https://cloud.google.com/functions/docs/calling/pubsub