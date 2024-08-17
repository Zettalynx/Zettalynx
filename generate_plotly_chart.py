import plotly.express as px
import pandas as pd

# Contoh data
df = pd.DataFrame({
    "Category": ["Repo A", "Repo B", "Repo C", "Repo D"],
    "Stars": [10, 20, 13, 7]
})

# Membuat bar chart
fig = px.bar(df, x='Category', y='Stars', title="Stars per Repository")

# Simpan grafik sebagai file HTML
fig.write_html("interactive_chart.html")
