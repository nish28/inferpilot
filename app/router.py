def choose_model(prompt: str, budget_priority: str, quality_level: str) -> tuple[str, str]:
    prompt_length = len(prompt)

    if quality_level == 'premium':
        return 'gpt-4o', 'Premium quality requested'

    if budget_priority == 'cost':
        return 'gpt-4o-mini', 'Cost optimized routing'

    if prompt_length > 1000:
        return 'gpt-4o', 'Large prompt routed to stronger model'

    return 'gpt-4o-mini', 'Balanced routing strategy'
