from customer_data.load_data import load_customer_data
from churn_prediction.model import ChurnPredictor
from segmentation.segment import segment_customers
from retention_strategy.strategy import match_strategy
from campaign_execution.execute import send_campaign

# Load data
data = load_customer_data('customer_data/customers.csv')

# Churn prediction
features = data[['Tenure', 'MonthlySpend', 'SupportTickets']]
target = data['Churn']
predictor = ChurnPredictor()
predictor.train(features, target)

# Add churn scores
data['ChurnScore'] = predictor.predict(features)

# Segment customers
data = segment_customers(data)

# Match retention strategies and execute campaigns
for _, row in data.iterrows():
    strategy = match_strategy(row['Segment'], row['ChurnScore'])
    send_campaign(row['CustomerID'], strategy)
