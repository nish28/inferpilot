def build_usage_summary(requests: list[dict]) -> dict:
    total_requests = len(requests)
    total_cost = sum(item.get('cost', 0) for item in requests)
    total_savings = sum(item.get('savings', 0) for item in requests)

    return {
        'total_requests': total_requests,
        'total_cost_usd': round(total_cost, 4),
        'estimated_savings_usd': round(total_savings, 4),
    }
