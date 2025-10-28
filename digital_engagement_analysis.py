import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_synthetic_data():
    np.random.seed(42)
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=30)
    platforms = ['Twitter', 'Instagram', 'Facebook']
    data = []
    for date in dates:
        for platform in platforms:
            impressions = np.random.randint(500, 2000)
            engagements = np.random.randint(50, 300)
            data.append({
                'date': date,
                'platform': platform,
                'impressions': impressions,
                'engagements': engagements,
                'engagement_rate': engagements / impressions
            })
    df = pd.DataFrame(data)
    return df


def analyze_data(df):
    summary = df.groupby('platform').agg({
        'impressions': 'sum',
        'engagements': 'sum'
    })
    summary['engagement_rate'] = summary['engagements'] / summary['impressions']
    print("Summary statistics by platform:")
    print(summary)
    # Plot engagement rates
    summary['engagement_rate'].plot(kind='bar', title='Engagement Rate by Platform')
    plt.ylabel('Engagement Rate')
    plt.xlabel('Platform')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    df = generate_synthetic_data()
    analyze_data(df)
