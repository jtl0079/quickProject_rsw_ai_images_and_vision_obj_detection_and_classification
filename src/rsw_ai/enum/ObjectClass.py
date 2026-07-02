from enum import Enum


class ObjectClass(Enum):
    CIRCLE = (0, "circle")
    TRIANGLE = (1, "triangle")
    SQUARE = (2, "square")

    def __init__(self, class_id: int, label: str):
        self.id = class_id
        self.label = label

    @classmethod
    def from_id(cls, class_id: int):
        for item in cls:
            if item.id == class_id:
                return item
        raise ValueError(f"Unknown class id: {class_id}")

    @classmethod
    def from_label(cls, label: str):
        for item in cls:
            if item.label == label:
                return item
        raise ValueError(f"Unknown label: {label}")
