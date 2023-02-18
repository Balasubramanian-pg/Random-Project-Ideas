# Imports
import numpy as np
import pandas as pd
import datetime as dt
import plotly.express as px
import re
from string import punctuation as punct
import warnings
warnings.filterwarnings('ignore')

# Data Check and EDA
df = pd.read_csv("/kaggle/input/data-analyst-job-postings-google-search/gsearch_jobs.csv")
df = df.drop(columns=["Unnamed: 0", "index"])

# Format lists
remove_punct = lambda x: x.translate(str.maketrans('', '', punct)).split()
df.extensions = df.extensions.apply(remove_punct)
df.description_tokens = df.description_tokens.apply(remove_punct)

# Format dates
df.date_time = pd.to_datetime(df.date_time)
df.insert(14, "time_ago", df.date_time.apply(lambda x: dt.datetime.today() - x))
df.sample(5)

# Data Pin Pointing
top = 10
skills = []
for val in df.description_tokens.values:
    skills.extend(val)
skills, counts = np.unique(skills, return_counts=True)
top_skill_count = sorted(zip(list(skills), list(counts)), key=lambda x: -x[1])[:top]
top_skills = list(map(lambda x: x[0], top_skill_count))
top_counts = list(map(lambda x: x[1], top_skill_count))
salaries = []
for skill in top_skills: 
    salaries.append(df[df.description_tokens.apply(lambda x: skill in x)].salary_standardized.mean())
top_skills_df = pd.DataFrame({"skill": list(top_skills), "number_of_postings": top_counts,"avg_yearly_salary": map(round, salaries)})
top_skills_df = top_skills_df.sort_values("avg_yearly_salary", ascending=False)
top_skills_df

# Data Visualization
fig = px.treemap(top_skills_df, path=['skill'], values='number_of_postings',
                  color='avg_yearly_salary', color_continuous_scale='Blues')

fig.update_traces(hovertemplate='Skill: %{label} <br> \
Postings: %{value} <br> Average yearly salary: %{color}<extra></extra>')

fig.update_layout(
    title_text="<b>Salaries for 10 most popular<br>Data Analytics skills</b>", 
    title_x=0.1, title_font_size = 24, font_color="white",
    paper_bgcolor="#444444", 
    coloraxis_colorbar=dict(title="Average yearly salary")
)

fig.show()  