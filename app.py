import streamlit as st
import pandas as pd
import plotly.express as px


# ===============================
# PAGE CONFIGURATION
# ===============================

st.set_page_config(
    page_title="GHG Emission Forecasting Dashboard",
    page_icon="🌍",
    layout="wide"
)


# ===============================
# LOAD DATA
# ===============================

@st.cache_data
def load_data():

    ghg_data = pd.read_csv(
        "data/ghg_features.csv"
    )

    model_results = pd.read_csv(
        "data/final_comparison.csv"
    )

    ets_forecast = pd.read_csv(
        "data/ets_forecasts.csv"
    )

    model_data = pd.read_csv(
        "data/model_data.csv"
    )

    scenario_projection = pd.read_csv(
    "data/scenario_projections.csv"
)

    scenario_summary = pd.read_csv(
    "data/scenario_impact_summary.csv"
)


    return (
    ghg_data,
    model_results,
    ets_forecast,
    model_data,
    scenario_projection,
    scenario_summary
)


ghg_data, model_results, ets_forecast, model_data, scenario_projection, scenario_summary = load_data()


# ===============================
# SIDEBAR
# ===============================

st.sidebar.title(
    "🌍 Navigation"
)


page = st.sidebar.radio(
    "Select Page",
    [
    "Overview",
    "Historical Trends",
    "Country Profile",
    "Forecast",
    "Scenario Analysis",
    "Model Comparison"
    ]
)

# ===============================
# OVERVIEW PAGE
# ===============================

if page == "Overview":

    st.title(
        "🌍 Greenhouse Gas Emissions Forecasting Dashboard"
    )


    st.markdown(
        """
        This dashboard analyzes historical greenhouse gas emission trends
        and presents future CO₂ emission forecasts.

        The project includes:

        - Exploratory Data Analysis
        - Feature Engineering
        - Machine Learning Forecasting
        - ETS(A,Ad,N) Time-Series Forecasting
        - Model Performance Comparison
        """
    )


    st.subheader(
        "📊 Key Project Metrics"
    )


    total_countries = ghg_data["country"].nunique()


    latest_year = ghg_data["year"].max()


    latest_data = ghg_data[
        ghg_data["year"] == latest_year
    ]


    total_co2 = latest_data["co2"].sum()


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Countries Analyzed",
            total_countries
        )


    with col2:

        st.metric(
            "Latest Data Year",
            int(latest_year)
        )


    with col3:

        st.metric(
            "Total CO₂ Emissions",
            round(total_co2,2)
        )


    st.subheader(
        "📁 Dataset Preview"
    )


    st.dataframe(
        ghg_data.head(10)
    )

    # ===============================
# HISTORICAL TRENDS PAGE
# ===============================

elif page == "Historical Trends":


    st.title(
        "📈 Historical CO₂ Emission Trends"
    )


    st.markdown(
        """
        This section shows historical CO₂ emission patterns
        for selected countries.

        Users can compare emission growth or reduction trends
        across multiple countries.
        """
    )


    countries = sorted(
        ghg_data["country"].unique()
    )


    selected_countries = st.multiselect(
        "Select Countries",
        countries,
        default=[
            "China",
            "India",
            "United States"
        ]
    )


    filtered_data = ghg_data[
        ghg_data["country"].isin(
            selected_countries
        )
    ]


    fig = px.line(

        filtered_data,

        x="year",

        y="co2",

        color="country",

        markers=True,

        title="Historical CO₂ Emissions by Country"

    )


    fig.update_layout(

        xaxis_title="Year",

        yaxis_title="CO₂ Emissions (MtCO₂)"

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.subheader(
        "Selected Country Data"
    )


    st.dataframe(
        filtered_data
    )

   # ===============================
# COUNTRY PROFILE PAGE
# ===============================

elif page == "Country Profile":


    st.title(
        "🌐 Country Emission Profile"
    )


    st.markdown(
        """
        This section provides detailed greenhouse gas emission
        analysis for an individual country.

        It includes historical emissions, per-capita emissions,
        yearly changes, and statistical summaries.
        """
    )


    selected_country = st.selectbox(
        "Select Country",
        sorted(
            ghg_data["country"].unique()
        )
    )


    country_data = (
        ghg_data[
            ghg_data["country"]
            ==
            selected_country
        ]
        .sort_values(
            "year"
        )
    )


    # -------------------------------
    # CO2 TREND
    # -------------------------------

    st.subheader(
        "CO₂ Emission Trend"
    )


    fig1 = px.line(

        country_data,

        x="year",

        y="co2",

        markers=True,

        title=f"{selected_country} CO₂ Emissions Over Time"

    )


    st.plotly_chart(
        fig1,
        use_container_width=True
    )



    # -------------------------------
    # CO2 PER CAPITA
    # -------------------------------

    st.subheader(
        "CO₂ Per Capita Trend"
    )


    fig2 = px.line(

        country_data,

        x="year",

        y="co2_per_capita",

        markers=True,

        title=f"{selected_country} CO₂ Per Capita"

    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )



    # -------------------------------
    # YOY CHANGE
    # -------------------------------

    st.subheader(
        "Year-over-Year CO₂ Change"
    )


    fig3 = px.bar(

        country_data,

        x="year",

        y="co2_yoy_pct_change",

        title=f"{selected_country} Annual CO₂ Percentage Change"

    )


    st.plotly_chart(
        fig3,
        use_container_width=True
    )



    # -------------------------------
    # STATISTICS
    # -------------------------------

    st.subheader(
        "Emission Statistics"
    )


    st.dataframe(
        country_data[
            [
                "co2",
                "co2_per_capita",
                "co2_yoy_pct_change"
            ]
        ]
        .describe()
    ) 

    # ===============================
# FORECAST PAGE
# ===============================

elif page == "Forecast":


    st.title(
        "🔮 ETS(A,Ad,N) CO₂ Emission Forecast"
    )


    st.markdown(
        """
        This section displays future CO₂ emission forecasts
        generated using the ETS(A,Ad,N) time-series model.

        Forecast period:

        2024 → 2043
        """
    )


    selected_country = st.selectbox(
        "Select Country",
        sorted(
            ets_forecast["Country"].unique()
        )
    )


    country_forecast = (
        ets_forecast[
            ets_forecast["Country"]
            ==
            selected_country
        ]
        .sort_values(
            "Year"
        )
    )


    # -------------------------------
    # FORECAST CHART
    # -------------------------------


    fig = px.line(

        country_forecast,

        x="Year",

        y="Forecast_CO2",

        markers=True,

        title=f"{selected_country} ETS CO₂ Forecast (2024-2043)"

    )


    fig.update_layout(

        xaxis_title="Year",

        yaxis_title="Forecast CO₂ Emissions (MtCO₂)"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



    # -------------------------------
    # FORECAST TABLE
    # -------------------------------


    st.subheader(
        "Forecast Values"
    )


    st.dataframe(
        country_forecast
    )


# ===============================
# SCENARIO ANALYSIS PAGE
# ===============================

elif page == "Scenario Analysis":

    st.title("🌍 Scenario Analysis")

    st.markdown("""
This section compares three future CO₂ emission pathways generated from the ETS(A,Ad,N) baseline forecast.

### Scenarios
- 🔵 Business As Usual (BAU)
- 🟠 Moderate Mitigation (2% annual reduction)
- 🟢 Aggressive Mitigation (5% annual reduction)

The mitigation scenarios apply compounded annual reductions beginning in 2025.
""")

    # ---------------------------------------
    # Country Selection
    # ---------------------------------------

    selected_country = st.selectbox(
        "Select Country",
        sorted(scenario_projection["Country"].unique())
    )

    # ---------------------------------------
    # Filter Data
    # ---------------------------------------

    country_projection = (
        scenario_projection[
            scenario_projection["Country"] == selected_country
        ]
        .sort_values(["Scenario", "Year"])
    )

    country_summary = (
        scenario_summary[
            scenario_summary["Country"] == selected_country
        ]
    )

    # ---------------------------------------
    # Scenario Line Chart
    # ---------------------------------------

    st.subheader("Scenario Projection")

    fig = px.line(

        country_projection,

        x="Year",

        y="CO2_Projected",

        color="Scenario",

        markers=True,

        color_discrete_map={
            "BAU": "blue",
            "Moderate": "orange",
            "Aggressive": "green"
        },

        title=f"{selected_country} CO₂ Emission Scenarios"

    )

    fig.update_layout(

        xaxis_title="Year",

        yaxis_title="Projected CO₂ Emissions (MtCO₂)"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ---------------------------------------
    # Projection Table
    # ---------------------------------------

    st.subheader("Scenario Projection Data")

    st.dataframe(
        country_projection,
        use_container_width=True
    )

    # ---------------------------------------
    # Cumulative Emissions Chart
    # ---------------------------------------

    st.subheader("Cumulative CO₂ Emissions (2025–2040)")

    fig2 = px.bar(

        country_summary,

        x="Scenario",

        y="Cumulative_CO2",

        color="Scenario",

        color_discrete_map={
            "BAU": "blue",
            "Moderate": "orange",
            "Aggressive": "green"
        },

        title=f"{selected_country} Cumulative Emissions"

    )

    fig2.update_layout(

        xaxis_title="Scenario",

        yaxis_title="Cumulative CO₂ Emissions"

    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.dataframe(
        country_summary,
        use_container_width=True
    )

    # ---------------------------------------
    # Global Scenario Comparison
    # ---------------------------------------

    st.subheader("Global Scenario Comparison")

    global_projection = (

        scenario_projection

        .groupby(
            ["Year", "Scenario"]
        )["CO2_Projected"]

        .sum()

        .reset_index()

    )

    fig3 = px.line(

        global_projection,

        x="Year",

        y="CO2_Projected",

        color="Scenario",

        markers=True,

        color_discrete_map={
            "BAU": "blue",
            "Moderate": "orange",
            "Aggressive": "green"
        },

        title="Global CO₂ Projection Under Different Scenarios"

    )

    fig3.update_layout(

        xaxis_title="Year",

        yaxis_title="Total Projected CO₂ Emissions"

    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )












# ===============================
# MODEL COMPARISON PAGE
# ===============================

elif page == "Model Comparison":


    st.title(
        "🤖 Forecasting Model Comparison"
    )


    st.markdown(
        """
        This section compares different forecasting approaches
        used in the project.

        Models compared:

        - Naive Baseline
        - Linear Regression
        - Random Forest Regression
        - ETS(A,Ad,N)

        Performance is evaluated using MAE and RMSE.
        """
    )


    # -------------------------------
    # MODEL RESULTS TABLE
    # -------------------------------


    st.subheader(
        "Model Performance Results"
    )


    st.dataframe(
        model_results
    )


    # -------------------------------
    # COUNTRY SELECTION
    # -------------------------------


    selected_country = st.selectbox(
        "Select Country",
        sorted(
            model_results["Country"].unique()
        )
    )


    country_result = model_results[
        model_results["Country"]
        ==
        selected_country
    ]



    # -------------------------------
    # MAE COMPARISON
    # -------------------------------


    mae_data = country_result[
        [
            "Baseline MAE",
            "LR MAE",
            "RF MAE",
            "ETS MAE"
        ]
    ].T.reset_index()


    mae_data.columns = [
        "Model",
        "MAE"
    ]


    fig1 = px.bar(

        mae_data,

        x="Model",

        y="MAE",

        title=f"{selected_country} Model MAE Comparison"

    )


    st.plotly_chart(

        fig1,

        use_container_width=True

    )



    # -------------------------------
    # RMSE COMPARISON
    # -------------------------------


    rmse_data = country_result[
        [
            "Baseline RMSE",
            "LR RMSE",
            "RF RMSE",
            "ETS RMSE"
        ]
    ].T.reset_index()


    rmse_data.columns = [
        "Model",
        "RMSE"
    ]


    fig2 = px.bar(

        rmse_data,

        x="Model",

        y="RMSE",

        title=f"{selected_country} Model RMSE Comparison"

    )


    st.plotly_chart(

        fig2,

        use_container_width=True

    )



    # -------------------------------
    # BEST MODEL
    # -------------------------------


    best_model = country_result[
        "Best Model"
    ].values[0]


    st.success(
        f"Best Performing Model for {selected_country}: {best_model}"
    )