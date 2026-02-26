from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    # Each artifact is a dict: {’name’: str, ’power’: int, ’type’: str}

    # def get_power(artifact: Dict) -> int:
    #     return artifact["power"]

    # sorted_list = sorted(artifacts, key=get_power, reverse=True)

    sorted_list = sorted(artifacts, key=lambda artifact: artifact["power"],
                         reverse=True)

    return sorted_list


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    #  Each mage is a dict: {’name’: str, ’power’: int, ’element’: str}

    filtered_mages = filter(lambda mage: mage["power"] >= min_power, mages)

    return filtered_mages


def spell_transformer(spells: List[str]) -> List[str]:
    transf_spells = map(lambda spell: "* " + spell + " *", spells)
    return list(transf_spells)


def mage_stats(mages: List[Dict]) -> Dict:
    min_power = min(mages, key=lambda mage: mage["power"])
    max_power = max(mages, key=lambda mage: mage["power"])
    # total_power = sum([mage["power"] for mage in mages])
    total_power = sum(map(lambda mage: mage["power"], mages))
    avg_power = round(total_power / len(mages), 2)
    return {"max_power": max_power["power"],
            "min_power": min_power["power"],
            "avg_power": avg_power}


if __name__ == "__main__":
    artifacts = [{'name': 'Lightning Rod', 'power': 84, 'type': 'relic'},
                 {'name': 'Fire Staff', 'power': 108, 'type': 'focus'},
                 {'name': 'Wind Cloak', 'power': 64, 'type': 'relic'},
                 {'name': 'Light Prism', 'power': 90, 'type': 'accessory'}]
    print("\nArtifacts: before sorting")
    print("\n".join([str(art) for art in artifacts]))
    sorted_artifatcs = artifact_sorter(artifacts)
    print("\nArtifacts: after sorting")
    print("\n".join([str(art) for art in sorted_artifatcs]))

    mages = [{'name': 'Alex', 'power': 74, 'element': 'fire'},
             {'name': 'Zara', 'power': 74, 'element': 'shadow'},
             {'name': 'Riley', 'power': 58, 'element': 'earth'},
             {'name': 'Rowan', 'power': 96, 'element': 'lightning'},
             {'name': 'Ember', 'power': 51, 'element': 'earth'}]
    print("\nMages: before filtering")
    print("\n".join([str(mage) for mage in mages]))
    min_power = 70
    sorted_mages = power_filter(mages, min_power)
    print(f"\nMages: after filtering (min_power = {min_power})")
    print("\n".join([str(mage) for mage in sorted_mages]))

    spells = ['freeze', 'flash', 'fireball', 'lightning']
    print("\nSpells: before transforming")
    print(spells)
    transf_spells = spell_transformer(spells)
    print("\nSpells: after transforming")
    print(transf_spells)

    print("\nMage stats:")
    print(f"{mage_stats(mages)}")
