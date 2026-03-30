import pandas as pd

def run_analysis(filepath):
    df = pd.read_csv("C:/Users/balqe/OneDrive/Desktop/new_retail_data.csv")

    # 🟢 مثال تنظيف (عدليه حسب داتك)
    df['date'] = pd.to_datetime(df['date'])

    # 🟢 حساب Recency
    reference_date = df['date'].max() + pd.Timedelta(days=1)

    rfm = df.groupby('customer_id').agg({
        'date': lambda x: (reference_date - x.max()).days,
        'transaction_id': 'count',
        'total_amount': 'sum'
    }).reset_index()

    rfm.columns = ['customer_id', 'Recency', 'Frequency', 'Monetary']

    # 🟢 تقسيم العملاء (بسيط)
    rfm['Segment'] = pd.qcut(rfm['Monetary'], 4, labels=[
        'Low Value', 'Mid Value', 'High Value', 'VIP'
    ])

    return rfm
