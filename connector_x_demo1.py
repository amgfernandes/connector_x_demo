#%%
import polars as pl
#%%

conn = ""postgresql://username:password@server:port/database"
query = "SELECT * FROM dvdrental.public.actor;"

pl.read_sql(query, conn)
# %%
