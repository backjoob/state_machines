

graph = {
    "START": {
        "A": "A",
    },
    "A": {
        "B": "B",
    },
    "B": {
        "C": "C",
    },
    "C": {
        "D": "D",
    },
    "D": {
        "E": "E",
        "END": "END",
    },
    "E": {
        "F": "F",
    },
    "F": {
        "E": "E",
        "END": "END",
    },
    "END": None,
}

final_states = set(["D", "F"])

accepted_history = []
total_history = []

current_state = "START"
while True:
    print()
    print(f"Current state: {current_state}")
    transition = input("Enter transition: ")
    if transition == "END":
        break
    total_history.append(transition)
    try:
        current_state = graph[current_state][transition]
        accepted_history.append(transition)
    except KeyError:
        print(f"Invalid transition: {transition}")

if current_state in final_states:
    print("Accepted.")
else:
    print("Not accepted.")
print(accepted_history)
print(total_history)
