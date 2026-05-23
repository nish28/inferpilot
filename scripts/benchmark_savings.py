from app.costs import estimate_cost


PROMPTS = [
    'Write a tweet about AI.',
    'Summarize a support ticket.',
    'Generate product description.',
]


def main():
    baseline = 0
    optimized = 0

    for prompt in PROMPTS:
        baseline += estimate_cost('gpt-4o', 500, 300)
        optimized += estimate_cost('gpt-4o-mini', 500, 300)

    savings = baseline - optimized

    print('Baseline Cost:', round(baseline, 4))
    print('Optimized Cost:', round(optimized, 4))
    print('Savings:', round(savings, 4))


if __name__ == '__main__':
    main()
