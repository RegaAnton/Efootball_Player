import json

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def score_player(player, attributes_weights):
    attrs = player.get("attributes", {})
    score = 0
    for attr, weight in attributes_weights.items():
        score += attrs.get(attr, 0) * weight
    return score

def load_players_from_json(file_path):
    return load_json(file_path)

def main():
    attributes_weights = load_json("AMF/attributes_weights_attackingMidfielder.json")
    players = load_players_from_json("AMF/attackingMidfielder.json")
    ranked_players = sorted(players, key=lambda p: score_player(p, attributes_weights), reverse=True)

    print("Pemain Terbaik :\n")
    for i, player in enumerate(ranked_players, 1):
        print(f"{i}. {player['name']} - Score: {score_player(player, attributes_weights):.2f}")

if __name__ == "__main__":
    main()