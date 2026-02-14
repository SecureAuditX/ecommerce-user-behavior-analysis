################################################
# E-commerce User Behavior Analysis  DashBoard #
################################################

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_score
import warnings
import io

warnings.filterwarnings("ignore")

# ---------- LOAD DATA ----------
@st.cache_data
def load_data():
    dtypes = {
        'user_id': 'int32',
        'item_id': 'int32',
        'item_category': 'int32',
        'behavior_type': 'category',
        'timestamp': 'int32'
    }

    df = pd.read_csv(
        r"C:\X-Files\Coding_File\Python\Final_Project.py\UserBehavior.csv",
        encoding="latin1",
        names=["user_id", "item_id", "item_category", "behavior_type", "timestamp"],
        header=None,
        dtype=dtypes,
        nrows=100000
    )
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    return df

df = load_data()

# ---------- SIDEBAR ----------
st.sidebar.title("User Filters")
behavior_types = df['behavior_type'].unique().tolist()
selected_behaviors = st.sidebar.multiselect("Select Behaviors", behavior_types, default=behavior_types)

# ---------- THEME CUSTOMIZATION ----------
theme = st.sidebar.radio("🎨 Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""<style>body { background-color: #111; color: white; }</style>""", unsafe_allow_html=True)

# ---------- MAIN ----------
st.title("🛒 E-commerce User Behavior Dashboard")

st.subheader("Raw Dataset (Top 100,000 rows)")
st.dataframe(df[df['behavior_type'].isin(selected_behaviors)].head(100000))

# ---------- RFM ANALYSIS ----------
buy_df = df[df['behavior_type'] == 'buy']
rfm = buy_df.groupby("user_id").agg({
    'timestamp': ['max', 'count']
}).reset_index()
rfm.columns = ['user_id', 'last_purchase_date', 'frequency']
reference_date = buy_df['timestamp'].max()
rfm['recency'] = (reference_date - rfm['last_purchase_date']).dt.days
rfm['monetary'] = rfm['frequency'] * (98 / 3.4)

# ---------- HISTOGRAMS ----------
st.subheader("RFM Distributions")

fig, ax = plt.subplots(1, 3, figsize=(18, 5))
ax[0].hist(rfm['recency'], bins=30, color='skyblue')
ax[0].set_title("Recency")
ax[1].hist(rfm['frequency'], bins=30, color='lightgreen')
ax[1].set_title("Frequency")
ax[2].hist(rfm['monetary'], bins=30, color='salmon')
ax[2].set_title("Monetary")
st.pyplot(fig)

# ---------- CLUSTERING ----------
rfm_norm = rfm[['recency', 'frequency', 'monetary']].copy()
scaler = MinMaxScaler()
rfm_scaled = scaler.fit_transform(rfm_norm)
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['cluster'] = kmeans.fit_predict(rfm_scaled)

# ---------- CLUSTER VISUALIZATION ----------
st.subheader("Boxplot by Cluster")
fig, ax = plt.subplots(1, 3, figsize=(18, 5))
for i, col in enumerate(['recency', 'frequency', 'monetary']):
    sns.boxplot(x='cluster', y=col, data=rfm, ax=ax[i], palette='Set2')
    ax[i].set_title(col.capitalize())
st.pyplot(fig)

# ---------- PIE CHART ----------
st.subheader("Cluster Distribution (Pie Chart)")
cluster_counts = rfm['cluster'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.pie(cluster_counts, labels=[f'Cluster {i}' for i in cluster_counts.index], autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# ---------- SEGMENT LABELING ----------
labels = {0: 'VIP', 1: 'Churn Risk', 2: 'Loyal', 3: 'At_Risk'}
rfm['segment'] = rfm['cluster'].map(labels)

# ---------- BAR PLOT ----------
st.subheader("Segment Distribution (Bar Plot)")
segment_counts = rfm['segment'].value_counts()
fig, ax = plt.subplots()
bars = ax.bar(segment_counts.index, segment_counts.values, color=sns.color_palette("pastel"))
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 5, str(height), ha='center', fontsize=10)
st.pyplot(fig)

# ---------- SEGMENT SUMMARY ----------
st.subheader("Segment RFM Averages (Heatmap + Table)")
segment_summary = rfm.groupby('segment')[['recency', 'frequency', 'monetary']].mean().round(2)
st.dataframe(segment_summary)

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(segment_summary, annot=True, cmap='YlGnBu', fmt=".1f", ax=ax)
st.pyplot(fig)

# ---------- TIME SERIES ANALYSIS ----------
st.subheader("📈 Time Series Analysis")

df_filtered = df[df['behavior_type'] == 'buy']
df_filtered['date'] = df_filtered['timestamp'].dt.date
df_filtered['month'] = df_filtered['timestamp'].dt.to_period('M').astype(str)

st.markdown("**Daily Purchase Trends**")
daily_counts = df_filtered.groupby('date').size()
st.line_chart(daily_counts)

st.markdown("**Monthly Purchase Trends**")
monthly_counts = df_filtered.groupby('month').size()
st.line_chart(monthly_counts)

# ---------- DOWNLOAD CLUSTERED DATA ----------
st.subheader("⬇ Download Clustered & Segmented Data")
csv_data = rfm.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download RFM Clustered CSV",
    data=csv_data,
    file_name='rfm_segmented.csv',
    mime='text/csv'
)

# ---------- METRICS ----------
st.sidebar.title("🔍 Dataset Summary")
st.sidebar.metric("Total Users", rfm.shape[0])
st.sidebar.metric("Date Range", f"{rfm['last_purchase_date'].min().date()} to {rfm['last_purchase_date'].max().date()}")

# ---------- OPTIONAL: Pairplot ----------
with st.expander("Show RFM Pairplot"):
    sns.pairplot(pd.DataFrame(rfm_scaled, columns=['recency', 'frequency', 'monetary']))
    st.pyplot(plt.gcf())
# ---------- MARKETING STRATEGY ----------
st.subheader("💡 Precision Marketing Strategies")

strategy_df = pd.DataFrame({
    "Segment": ["VIP", "Loyal", "Churn Risk", "At_Risk"],
    "Behavior Description": [
        "High frequency, high monetary, recent buyers",
        "Repeat customers, moderate spenders",
        "Previously active, now disengaged",
        "Infrequent, low spenders"
    ],
    "Marketing Strategy": [
        "Offer exclusive access, early product launches, loyalty rewards",
        "Upsell/Cross-sell with relevant recommendations and reviews",
        "Win-back email campaigns, special reactivation offers",
        "Use retargeting ads, time-limited discounts to re-engage"
    ]
})

st.dataframe(strategy_df)

# Download button
strategy_csv = strategy_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇ Download Strategy CSV",
    data=strategy_csv,
    file_name="marketing_strategies.csv",
    mime="text/csv"
)
