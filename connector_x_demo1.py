#%%
import polars as pl
#%%

conn = "postgresql://postgres:sql@localhost:5432/dvdrental"
query = "SELECT * FROM dvdrental.public.actor"
#%%
df= (pl.read_sql(query, conn).lazy())
print(df.head(10))
# %%
df.head().collect()
# %%
