class FSTState:
    def __init__(self, id: int, is_final: bool, transitions: dict) -> None:
        self.id = id
        self.is_final = is_final
        self.transitions = transitions

    def next_id(self, letter) -> int:
        return self.transitions[letter]

    def is_final(self) -> bool:
        return self.is_final
