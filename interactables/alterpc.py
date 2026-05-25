from template.interactable import Interactable
from template.disk import Disk
from core.gamestate import GameState
from colorama import Fore,Style
from time import sleep
import os
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from template.item import Item

class AlterPc(Interactable):
    
    def __init__(self):
        super().__init__(
            name="Alter PC",
            description="Ein alter PC mit Bananen OS",
            items=None,
            locked=False
        )
    
    def command_help(self):
        print(f"""
 Commands:
 help      Show this menu
 disk      Play the inserted disk
 shutdown  Shutdown the PC
 More commands in progress!
""")

    def use(self, state: GameState, ram: bool, disk: Disk) -> List["Item"]:
        
        print(f"\nDu startest den PC...")
        sleep(2)
        print()
        print(f"{Style.BRIGHT} BANANEN OS{Style.RESET_ALL}")
        sleep(0.5)
        print(f" Booting...")
        sleep(3)
        if ram:
            print(f" Finished Booting!")
            print()
            print(f"{Style.BRIGHT} Please login!")
            print(f" Username: pc_banana")
            password = input(f" Password: ")
            if password == "b4Nan3!":
                print(f"{Style.RESET_ALL} Thanks for logging in!\n")
                if disk == None:
                    print(f" Disk: {Fore.RED}No Disk detected{Style.RESET_ALL}")
                else:
                    print(f" Disk: {disk.name}")
                self.command_help()
                running = True
                while running:
                    eingabe = input(f" >> ")
                    eingabe = eingabe.strip().lower()
                    if eingabe == "help":
                        self.command_help()
                    elif eingabe == "disk":
                        if disk == None:
                            print(f"{Fore.RED} No disk inserted!{Style.RESET_ALL}")
                        else:
                            print(f" Starting Disk '{disk.name}'")
                            sleep(1)
                            print()
                            disk.play()
                            print()
                            print(f" Ending Disk '{disk.name}'")
                            
                    elif eingabe == "shutdown":
                        print(f" Thanks for using Bananen OS!")
                        running = False
                    else:
                        print(f"{Fore.Red} Command not recognized!\n Use 'help' to look at all commands.")
            else:
                print(f"{Style.RESET_ALL}{Fore.RED} Incorrect Password!")
        else:
            print(f"{Fore.RED}{Style.BRIGHT} !!! No RAM detected !!!{Style.RESET_ALL}")

        sleep(1)
        print(f"{Style.RESET_ALL} Shutting down...")
        sleep(3)
        print(f"\nDer Bildschirm wird schwarz...")

        
        