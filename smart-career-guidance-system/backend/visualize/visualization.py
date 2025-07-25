import plotly.express as px

def plot_trend(df_time, df_region, skill_counts, companies):
    fig_time = px.line(df_time, x='date', y=df_time.columns[1], title="Interest Over Time")
    fig_region = px.choropleth(df_region, locations='geoName', color=df_region.columns[1], title="Global Interest")
    if not skill_counts:
        skill_counts = [("No Data", 0)]
    skills, counts = zip(*skill_counts)
    fig_skills = px.bar(x=skills, y=counts, title="Top Required Skills in Job Posts")
    if not companies:
        companies = [("No Data", 0)]
    comps, comp_counts = zip(*companies)
    fig_companies = px.bar(x=comps, y=comp_counts, title="Top Companies Hiring")
    return fig_time, fig_region, fig_skills, fig_companies
