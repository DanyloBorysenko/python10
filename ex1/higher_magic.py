import itertools
import functools
import operator
from typing import Callable, Tuple, Any, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args: Any, **kwargs: Any) -> Tuple[Any, Any]:
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args: Any, **kvargs: Any) -> int:
        base_res = base_spell(*args, **kvargs)
        return base_res * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def casted(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return casted


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell_all(*args: Any, **kwargs: Any) -> List[Any]:
        return [spell(*args, **kwargs) for spell in spells]
    return spell_all


if __name__ == "__main__":
    #  combiner
    print("Testing spell combiner...")
    target = "Dragon"

    def spell1(target: str) -> str:
        return "Fireball hits " + target

    def spell2(target: str) -> str:
        return "Heals " + target

    combined: Callable = spell_combiner(spell1, spell2)
    print(f"Combined spell result: {combined(target)}")

    #  amplifier
    print("\nTesting power amplifier...")
    original = 15

    def power(value: int) -> int:
        return value

    amplified: Callable = power_amplifier(power, 2)
    print(f"Original: {original}, Amplified: {amplified(original)}")

    #  caster
    print("\nTesting conditional caster...")

    def spell(target: str, damage: int) -> str:
        return f"Target: {target}, damage: {damage}"

    def condition(target: str, damage: int) -> bool:
        return True if target == "Dragon" else False

    casted: Callable = conditional_caster(condition, spell)
    print(casted("Dragon", damage=20))
    print(casted("Goblin", damage=20))

    #  sequence
    print("\nTesting spell sequence...")
    spells = [spell1, spell2]
    spell_all: Callable = spell_sequence(spells)
    print(spell_all("Dragon"))
