import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px

st.set_page_config(page_title="AquaGuard National Portal", layout="wide")

# ---------- Header ----------
st.markdown("""
<h1 style='text-align:center;'>🇮🇳 AquaGuard National Water Monitoring Portal</h1>
<p style='text-align:center;'>Supporting informed decisions for sustainable water management</p>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
st.sidebar.header("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Dashboard","India Map","Analytics","State Lookup","Insights","Citizen Guide"]
)

# ---------- Paths ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "processed", "india_water_risk.csv")
geo_path = os.path.join(BASE_DIR, "data", "india_states.geojson")

df = pd.read_csv(data_path)

def classify(x):
    if x < 55:
        return "High Risk"
    elif x < 70:
        return "Moderate Risk"
    else:
        return "Low Risk"

df["Risk Level"] = df["water_availability"].apply(classify)

# ---------- Dashboard ----------
if page == "Dashboard":

    st.subheader("📊 National Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("States Monitored", len(df))
    col2.metric("High Risk", (df["Risk Level"] == "High Risk").sum())
    col3.metric("Moderate Risk", (df["Risk Level"] == "Moderate Risk").sum())

    st.warning("⚠ Continuous monitoring recommended in vulnerable regions.")

# ---------- Map ----------
elif page == "India Map":

    st.subheader("🗺 Water Risk Map")

    with open(geo_path) as f:
        india_geo = json.load(f)

    fig_map = px.choropleth(
        df,
        geojson=india_geo,
        featureidkey="properties.NAME_1",
        locations="state",
        color="water_availability",
        color_continuous_scale="YlOrRd",
    )

    fig_map.update_geos(fitbounds="locations", visible=False)

    st.plotly_chart(fig_map, width="stretch")

    st.caption("Darker shades indicate higher water stress.")

# ---------- Analytics ----------
elif page == "Analytics":

    st.subheader("📈 Data Analysis")

    st.bar_chart(df.set_index("state")["water_availability"])

    rain_change = st.slider("Rainfall change scenario (%)", -50, 50, 0)

    df["Predicted"] = df["water_availability"] * (1 + rain_change/100)

    st.line_chart(df.set_index("state")["Predicted"])

# ---------- State Lookup ----------
elif page == "State Lookup":

    state = st.selectbox("Select a state", df["state"])

    result = df[df["state"] == state]

    st.write(result)

# ---------- Insights ----------
elif page == "Insights":

    st.subheader("🏛 Policy Insights")

    st.info("""
    Regions with elevated risk should strengthen groundwater recharge,
    drought planning, and water efficiency initiatives.
    """)

    st.dataframe(df[["state","Risk Level"]])

# ---------- Citizen Guide ----------
elif page == "Citizen Guide":

    st.subheader("💧 Water Conservation Tips")

    st.success("""
    ✔ Use water responsibly  
    ✔ Harvest rainwater  
    ✔ Fix leaks promptly  
    ✔ Reduce wastage  
    """)

# ---------- Download ----------
st.sidebar.download_button(
    label="Download Data Report",
    data=df.to_csv(index=False),
    file_name="india_water_report.csv",
    mime="text/csv"
)

# ---------- Footer ----------
st.markdown("""
<hr>
<p style='text-align:center;'>AquaGuard — Supporting sustainable water futures</p>
""", unsafe_allow_html=True)
