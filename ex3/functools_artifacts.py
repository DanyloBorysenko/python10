
from functools import lru_cache, partial, reduce, singledispatch
import operator
from typing import Dict, Callable, List, Any
import time


def spell_reducer(spells: List[int], operation: str) -> int:
    operations = {"add": operator.add,
                  "multiply": operator.mul,
                  "max": lambda a, b: (a, b)[operator.gt(b, a)],
                  "min": lambda a, b: (a, b)[operator.lt(b, a)]}
    if operation not in operations:
        return
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment,
                                power=50, element="fire"),
        "ice_enchant": partial(base_enchantment,
                               power=50, element="ice"),
        "lightning_enchant": partial(base_enchantment,
                                     power=50, element="lightning")
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:

    @singledispatch
    def dispatcher(a: Any) -> None:
        raise TypeError(f"Unknown spell type: {type(a)}")

    @dispatcher.register(int)
    def _(damage: int) -> None:
        print(f"Damage spell cast! Dealing {damage} damage.")

    @dispatcher.register(str)
    def _(enchantment: str) -> None:
        print(f"Enchantment applied: {enchantment}")

    @dispatcher.register(list)
    def _(spells: List) -> None:
        print(f"Multi-cast! Casting {len(spells)} spells.")
    return dispatcher


if __name__ == "__main__":
    #  spell_reducer
    print("Testing spell_reducer...")
    spell_powers = [25, 2]
    operations = ['add', 'multiply', 'max', 'min']
    for oper in operations:
        print(f"Operation '{oper}': "
              f"result = {spell_reducer(spell_powers, oper)}")

    #  partial_enchanter
    print("\nTesting partial_enchanter...")

    def cast_spell(power: int, element: str, target: str) -> str:
        return f"Casting {element} (Power: {power}) on {target}!"

    enchanters = partial_enchanter(cast_spell)

    res = enchanters["fire_enchant"](target="Dragon")
    print(res)

    #  memoized_fibonacci
    print("\nTesting memoized_fibonacci...")
    print("First call")
    start = time.perf_counter()
    print(f"{memoized_fibonacci(30)}")
    end = time.perf_counter()
    print(f"Time = {end - start:.8f} seconds")

    print("Second call")
    start = time.perf_counter()
    print(f"{memoized_fibonacci(30)}")
    end = time.perf_counter()
    print(f"Time = {end - start:.8f} seconds")

    #  spell_dispatcher
    print("\nTesting spell_dispatcher...")
    dispatcher = spell_dispatcher()
    dispatcher(20)
    dispatcher("fireball")
    dispatcher([30, "fireball"])
