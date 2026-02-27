from typing import Callable, Any
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
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
            if args[0] >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    pass


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass


def cast_spell(self, spell_name: str, power: int) -> str:
    pass


if __name__ == "__main__":
    #  spell_timer
    print("Testing spell_timer...")

    @spell_timer
    def count_to_1000() -> int:
        res = 0
        for _ in range(10000):
            res += 1
        return res
    print(f"{count_to_1000()}")

    #  power_validator
    print("\nTesting power_validator...")

    @power_validator(10)
    def spell(power: int, target: str) -> str:
        return f"Power: {power}, Target: {target}"

    print(spell(5, "Dragon"))
    print(spell(10, "Dragon"))


# Enter your choice: 4
# === Exercise 4 Test Data ===
# # Master's Tower Test Data
# test_powers = [20, 15, 6, 12]
# spell_names = ['tsunami', 'blizzard', 'darkness', 'shield']
# mage_names = ['Ash', 'Alex', 'Storm', 'Nova', 'Kai', 'Morgan']
# invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']