class Robot:
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.parts=[
            Part("Head", attack_level=5, defense_level=10, energy_consumption=5),
            Part("Weapon", attack_level=15, defense_level=0, energy_consumption=10),
            Part("Left arm", attack_level=3, defense_level=20, energy_consumption=10),
            Part("Right arm", attack_level=6, defense_level=20, energy_consumption=10),
            Part("Left leg", attack_level=4, defense_level=20, energy_consumption=15),
            Part("Right leg", attack_level=8, defense_level=20, energy_consumption=15),
        ]

    def print_robot(self):
        import random 

        robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}                              
      Defense: {head_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     __     |    __          |Attack: {weapon_attack}
    |oooo| ______ |oooo| ------> |Defense: {weapon_defense}
    |oooo|' .  . '|oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|          
    `----' / __ \ '----´           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|   \'          |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/   \          |Attack: {left_arm_attack}
  / \_/ ||| |/\| ||| \_/  \         |Defense: {left_arm_defense}
 |\/     O\=----=/O      \/|        |Energy consumption: {left_arm_energy_consump}
 <>        |=\/=|        <> ------> |
 <>       |------|       <>         |3: {right_arm_name}
|  |   _ |======| _   |  |        |Is available: {right_arm_status}
//\\  / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
\_/  ||||        ||||  \_/        
      ||||        ||||          |4: {left_leg_name} 
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      ><            ><           |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
    |\/|_      |\/|_        |Is available: {right_leg_status}
   /_n_n\    /n_n_\       |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consump}
                                
"""

        status_dict = self.get_status_part()
        print(robot_art.format_map(status_dict))
        
    def display_menu(self):
        print("===== MENU =====")
        print("1. Attack a part")
        print("2. Show robot status")
        print("3. Exit")
        print("================")


    def attack_phase(self):
        attacking_part_name = input("Enter the name of the part you want to use for the attack: ")
        target_part_name = input("Enter the name of the part you want to attack: ")

        attacking_part = self.find_part_by_name(attacking_part_name)
        target_part = self.find_part_by_name(target_part_name)

        if not attacking_part:
            print(f"Invalid part name: {attacking_part_name}. Attack canceled.")
            return

        if not target_part:
            print(f"Invalid part name: {target_part_name}. Attack canceled.")
            return

        if self.energy < attacking_part.energy_consumption:
            print(f"Your {self.name} doesn't have enough energy to attack with {attacking_part.name}")
            return

        self.energy -= attacking_part.energy_consumption

        if attacking_part.name == "Weapon":
            target_part.energy_consumption = 0
            target_part.defense_level = 0
        else:
            target_part.defense_level -= attacking_part.attack_level

        self.display_status()  

    def find_part_by_name(self, part_name):
        for part in self.parts:
            if part_name == part.name:
                return part
        return None 
           
    def get_status_part(self):
            part_status = {}
            for part in self.parts:
                status_dict = part.get_status_part()
                part_status.update(status_dict)
            return part_status

class Part():
    def __init__(self, name, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption
        
    def shield(self):
        if  self.defense_level >= 0:
            return True
        else:
            return False
        
colors = {
    "Black": '\x1b[90m',
    "Blue": '\x1b[94m',
    "Cyan": '\x1b[96m',
    "Green": '\x1b[92m',
    "Magenta": '\x1b[95m',
    "Red": '\x1b[91m',
    "White": '\x1b[97m',
    "Yellow": '\x1b[93m',
}
def run_game(self):
    print("Welcome to the Robot Battle Game!")
    while True:
        self.display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            self.attack_phase()
        elif choice == "2":
            self.print_robot()
        elif choice == "3":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    
    robot_1 = Robot(input("Name of the player1: "), colors["Red"])
    robot_2 = Robot(input("Name of the player2: "), colors["Red"])
    Robot.run_game()
    
