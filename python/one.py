class DigraphImpl:
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

    @classmethod
    def interact(cls):
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
                current_state = cls.graph[current_state][transition]
                accepted_history.append(transition)
            except KeyError:
                print(f"Invalid transition: {transition}")

        if current_state in cls.final_states:
            print("Accepted.")
        else:
            print("Not accepted.")
        print(accepted_history)
        print(total_history)

class ClassImpl:
    class A:
        def B(self):
            self.__class__ = ClassImpl.B
    class B:
        def C(self):
            self.__class__ = ClassImpl.C
    class C:
        def D(self):
            self.__class__ = ClassImpl.D
    class D:
        def E(self):
            self.__class__ = ClassImpl.E
        def END(self):
            return True
    class E:
        def F(self):
            self.__class__ = ClassImpl.F
    class F:
        def E(self):
            self.__class__ = ClassImpl.E
        def END(self):
            return True
    @staticmethod
    def interact():
        sm = ClassImpl.A()
        while True:
            print()
            print(f"Current state: {sm.__class__}")
            try:
                if getattr(sm, input("Enter transition: "))():
                    break
            except AttributeError:
                print("Invalid transition.")

if __name__ == "__main__":
    DigraphImpl.interact()
    ClassImpl.interact()
