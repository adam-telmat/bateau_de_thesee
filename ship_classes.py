from typing import Dict
from datetime import datetime

class Part:
    def __init__(self, name: str, material: str):
        self.name = name
        self.material = material
        self.installation_date = datetime.now()

    def change_material(self, new_material: str) -> None:
        self.material = new_material
        self.installation_date = datetime.now()

    def __str__(self) -> str:
        return f"{self.name} (en {self.material}, installé le {self.installation_date.strftime('%d/%m/%Y')})"

class Ship:
    def __init__(self, name: str):
        self.name = name
        self.__parts: Dict[str, Part] = {}
        self.__modifications_history = []
        
    def add_part(self, part: Part) -> None:
        self.__parts[part.name] = part
        self.__modifications_history.append(
            f"{datetime.now().strftime('%d/%m/%Y %H:%M')} - Ajout de {part}"
        )

    def display_state(self) -> None:
        print(f"\nÉtat du navire {self.name}:")
        for part in self.__parts.values():
            print(f"- {part}")

    def replace_part(self, part_name: str, new_part: Part) -> None:
        if part_name in self.__parts:
            old_part = self.__parts[part_name]
            self.__parts[part_name] = new_part
            self.__modifications_history.append(
                f"{datetime.now().strftime('%d/%m/%Y %H:%M')} - Remplacement de {old_part} par {new_part}"
            )
        else:
            raise ValueError(f"La pièce {part_name} n'existe pas sur ce navire")

    def change_part(self, part_name: str, new_material: str) -> None:
        if part_name in self.__parts:
            part = self.__parts[part_name]
            old_material = part.material
            part.change_material(new_material)
            self.__modifications_history.append(
                f"{datetime.now().strftime('%d/%m/%Y %H:%M')} - Modification du matériau de {part_name} : {old_material} -> {new_material}"
            )
        else:
            raise ValueError(f"La pièce {part_name} n'existe pas sur ce navire")

    def get_history(self) -> list:
        return self.__modifications_history

class RacingShip(Ship):
    def __init__(self, name: str, max_speed: float):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self) -> None:
        print(f"\nVitesse maximale du {self.name}: {self.max_speed} nœuds") 