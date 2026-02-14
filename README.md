# 🛍️ E-commerce User Behavior Analysis Dashboard
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
Welcome to the **E-commerce User Behavior Analysis Dashboard**, a powerful data analytics and customer segmentation tool built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**. It transforms raw user behavior data into actionable insights for marketing strategy, business growth, and retention.

![Ecommerce](https://github.com/SecureAuditX/E-commerce-User-Behavior-Analysis/blob/c2730bada7cb68f537d9b1c48e6bca5ade950cb7/Ecommerce.png)
---

## 🎯 Project Objectives

- Analyze user behavior (view, cart, buy, etc.) on an e-commerce platform.
- Perform **RFM Analysis** to segment users based on Recency, Frequency, and Monetary value.
- Use **K-Means Clustering** to group users into meaningful segments.
- Visualize user segments and trends with an interactive **dashboard**.
- Suggest **targeted marketing strategies** per customer segment.
- Allow business stakeholders to **download segmented reports** for operational use.

---

## 🧰 Technologies & Libraries Used

- **Python 3**
- **Pandas, NumPy** – Data manipulation
- **Matplotlib, Seaborn** – Visualizations
- **Scikit-learn** – Clustering & Scaling
- **Streamlit** – Interactive dashboard UI
- **Colorama, IPython.display** – Aesthetic enhancements
- **CSV** – Data download & export

---

## 📊 Features

### 🔍 Behavior Filter
- Select specific behavior types (e.g. *view*, *cart*, *buy*) from the sidebar.

### 🎨 Theme Customization
- Switch between Light and Dark modes.

### 📈 Dashboard Visualizations
- Raw dataset viewer
- RFM Histograms
- Clustering boxplots
- Cluster distribution pie chart
- Segment distribution bar plot
- Heatmap and table summary of RFM by segment
- Daily & Monthly time series purchase trends

### 💾 Downloads
- Download **clustered user data** (`rfm_segmented.csv`)
- Download **marketing strategies per segment** (`marketing_strategies.csv`)

### 💡 Precision Marketing Suggestions
| Segment    | Description                                 | Strategy |
|------------|---------------------------------------------|----------|
| **VIP**    | High frequency, high spend, recent buyers   | Loyalty rewards, early access |
| **Loyal**  | Repeat customers, moderate spenders         | Upsell/cross-sell |
| **Churn Risk** | Previously active, now disengaged    | Win-back campaigns |
| **At_Risk**| Infrequent, low spenders                    | Retargeting, discounts |

---

## 📁 Project Structure

```
📦 E-commerce-User-Behavior-Analysis
├── 📊 analysis_notebook.ipynb        # Core data analysis & clustering logic
├── 📈 dashboard_app.py               # Streamlit-based dashboard (uploaded)
├── 📄 UserBehavior.csv               # Dataset (100,000 sampled rows)
└── README.md                         # You’re here!
```

---

## 🚀 How to Run the Project

> ⚠️ Make sure you have Python 3.8+ and `pip` installed.

### 1. Install Requirements

```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn
```

### 2. Run the Dashboard

```bash
streamlit run dashboard_app.py
```

The dashboard will open in your browser at `http://localhost:8501`.

---

## 🧠 Sample Use Cases

- 👩‍💼 **Marketing Teams** – Discover user segments and tailor campaigns
- 🧑‍💻 **Product Managers** – Understand engagement trends
- 📈 **Data Analysts** – Run deeper behavioral segmentation experiments

---

## 🛠 Future Improvements

- ✅ Add login authentication to secure dashboard access
- 📦 Deploy on the web (e.g. Streamlit Cloud or Heroku)
- 🔍 Include more advanced clustering (e.g. DBSCAN, Hierarchical)
- 🧠 Add machine learning to predict customer churn

---


## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 📬 Contact

Feel free to connect with me:

- GitHub: [SecureAuditX](https://github.com/SecureAuditX)
- LinkedIn: [Abdulkarim Umar](https://www.linkedin.com/in/abdulkarim-umar-14789937b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)
- Email: _(abdulkarimumar86@gmail.com)_
