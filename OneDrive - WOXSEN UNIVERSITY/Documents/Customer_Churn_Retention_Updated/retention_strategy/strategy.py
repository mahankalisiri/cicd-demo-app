def match_strategy(segment, churn_score):
    if churn_score > 0.8:
        if segment == 0:
            return "Offer loyalty discount"
        elif segment == 1:
            return "Give premium support"
        else:
            return "Send retention email"
    elif churn_score > 0.5:
        return "Engage with survey"
    else:
        return "No action needed"
