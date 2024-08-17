import plotly.express as px
import pandas as pd

# Data contoh
df = pd.DataFrame({
    "Category": ["Repo A", "Repo B", "Repo C", "Repo D"],
    "Stars": [10, 20, 13, 7]
})

# Membuat bar chart
fig = px.bar(df, x='Category', y='Stars', title="Stars per Repository")

# Simpan grafik sebagai gambar PNG
fig.write_image("data_visualization.png")
