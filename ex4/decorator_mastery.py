from typing import Callable, Any
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    # @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # """it is just a wrapper"""
        print(f"Casting '{func.__name__}'...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.6f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")
            if power is None:
                if args is None:
                    raise ValueError("No arguments")
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break
                    raise ValueError("power argument was not received")
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(max_attempts):
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {i + 1}/{max_attempts})")
            return "Spell casting failed after max_attempts attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        char_count = 0
        for char in name:
            if char == " ":
                continue
            if not char.isalpha():
                return False
            char_count += 1
        return char_count >= 3

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == "__main__":
    #  spell_timer
    print("Testing spell_timer...")

    @spell_timer
    def count_to_1000() -> int:
        # """iterate over numbers from 0 to 99 and add every num to res"""
        res = 0
        for _ in range(1000):
            res += 1
        return res
    print(f"{count_to_1000()}")
    # print(count_to_1000.__doc__)

    #  power_validator
    print("\nTesting power_validator...")

    @power_validator(10)
    def spell(power: int, target: str) -> str:
        return f"Power: {power}, Target: {target}"

    print(spell(5, "Dragon"))
    print(spell(10, "Dragon"))

    #  retry_spell
    print("\nTesting retry_spell...")

    @retry_spell(5)
    def funct_with_exception(spell: str) -> None:
        raise ValueError("Custom exception")

    @retry_spell(5)
    def funct_without_exception(spell: str) -> str:
        return f"Spell '{spell}' was used"

    print("\nTesting function with exception")
    print(funct_with_exception("Fire"))

    print("\nTesting function without exception")
    print(funct_without_exception("Fire"))

    #  MageGuild
    print("\nTesting MageGuild class...")
    mage_guild = MageGuild()
    print(mage_guild.validate_mage_name("correct name"))
    print(mage_guild.cast_spell(power=15, spell_name="fire"))
    print(mage_guild.cast_spell(power=5, spell_name="fire"))
