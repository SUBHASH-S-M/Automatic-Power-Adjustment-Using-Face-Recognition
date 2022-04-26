import pandas as pd
df=pd.read_excel("Database.xlsx")
face_id="subhash"
left="2.5"
right="3.5"

df.loc[len(df.index)] = [len(df)+1, right, left] 
df.to_excel("Database.xlsx")

