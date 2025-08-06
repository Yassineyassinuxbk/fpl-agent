def suggest_transfers(current_team):
    # Very basic logic - replace lowest scoring player with random one
    import random
    if not current_team:
        return []
    to_transfer_out = min(current_team, key=lambda x: x['points'])
    # Simulate suggestion
    suggested_transfer = {
        "out": to_transfer_out["element"],
        "in": random.randint(1, 600)  # Simulated player ID
    }
    return [suggested_transfer]
