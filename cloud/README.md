`gcloud auth login`

`gcloud condif set project PROJECT_ID`

`gcloud functions deploy search_fii_reports --trigger-topic search-fii-reports --runtime python37`

# Testando

`gcloud functions call search_fii_reports --data '{"topic":"search-fii-reports","message":"Hello World!", "data": {"stocks": ["GGRC", "FLMA", "VISC", "WPLZ", "MXRF", "RBRR", "RBRF", "UBSR", "ALZR", "BRCR", "HGLG", "HGRU", "HGRE"], "base_date": "2020-12-30"}}'`

// eyJzdG9ja3MiOiBbIkdHUkMiLCAiRkxNQSIsICJWSVNDIiwgIldQTFoiLCAiTVhSRiIsICJSQlJSIiwgIlJCUkYiLCAiVUJTUiIsICJBTFpSIiwgIkJSQ1IiLCAiSEdMRyIsICJIR1JVIiwgIkhHUkUiXSwgImJhc2VfZGF0ZSI6ICIyMDIwLTEyLTMwIn0=


# ver logs

`gcloud functions logs read search_fii_report`

# Referências

- https://cloud.google.com/functions/docs/calling/pubsub