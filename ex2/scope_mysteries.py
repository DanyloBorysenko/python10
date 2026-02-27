from typing import Callable, Dict, Any


def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


# def spell_accumulator(initial_power: int) -> Callable:
#     total_power: int = initial_power

#     def power_counter(given_power: int) -> int:
#         nonlocal total_power
#         total_power += given_power
#         return total_power
#     return power_counter

def spell_accumulator(initial_power: int) -> Callable:
    total_power: int = initial_power

    def power_counter() -> int:
        nonlocal total_power
        total_power += initial_power
        return total_power
    return power_counter


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return apply_enchantment


def memory_vault() -> Dict[str, Callable]:
    pairs: Dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        pairs[key] = value

    def recall(key: Any) -> Any:
        value = pairs.get(key, "Memory not found")
        return value
    return {"store": store, "recall": recall}


# def main() -> Callable:
#     name: str = "Anna"
#     age: int = 43

#     def inner() -> None:
#         print(f"{len(name)}")
#         print(f"{True if age > 18 else False}")
#     return inner


if __name__ == "__main__":
    #  mage_counter
    print("Testing mage_counter...")
    counter = mage_counter()
    # print(f"{counter.__closure__[0].cell_contents}")
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    #  spell_accumulator
    print("\nTesting spell_accumulator...")
    power_counter = spell_accumulator(2)
    # print(f"{power_counter.__closure__[0].cell_contents}")
    print(f"Call 1: {power_counter()}")
    print(f"Call 2: {power_counter()}")

    #  enchantment_factory
    print("\nTesting enchantment_factory...")

    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")
    print(f"{flaming_factory("Sword")}")
    print(f"{frozen_factory("Shield")}")

    #  memory_vault
    print("\nTesting memory_vault...")

    pair1 = ("danborys", "+420777...")
    pair2 = ("Den", 25)
    actions: Dict[str, Callable] = memory_vault()
    store_operation = actions["store"]
    recall_operation = actions["recall"]

    store_operation(*pair1)
    store_operation(*pair2)

    print(f"Value for key 'danborys' - {recall_operation("danborys")}")
    print(f"Value for key 'Den' - {recall_operation("Den")}")
    print(f"Value for key 'Martin' - {recall_operation("Martin")}")

    # inner = main()
    # print(inner.__closure__[0].cell_contents)
    # print(inner.__closure__[1].cell_contents)
