import pandas as pd

prov_df = pd.read_csv('tbs-prov-std/Canadian_prov_terr_du_Canada.csv') \
    .set_index('code')
prov_df.to_json('prov.json', orient='index')