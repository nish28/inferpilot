MODEL_PRICING = {
    'gpt-4o': {
        'input': 0.005,
        'output': 0.015,
    },
    'gpt-4o-mini': {
        'input': 0.00015,
        'output': 0.0006,
    },
}


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    pricing = MODEL_PRICING.get(model)

    if not pricing:
        return 0

    input_cost = (input_tokens / 1000) * pricing['input']
    output_cost = (output_tokens / 1000) * pricing['output']

    return round(input_cost + output_cost, 6)
