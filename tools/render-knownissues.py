import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSjwgWch-VUNzg8i1fQ_BK7Gnge-qipRQaW-xfdSwykJROjWu8Q9HiRFyeBgtnjK22FsnAPoFS08Vkd/pub?gid=101201913&single=true&output=csv"
df = pd.read_csv(url)

html = df.to_html(
    index=False,
    classes="compact-table",
    border=0
)

with open("../docs/changelog/generated_table.html", "w") as f:
    f.write(html)
