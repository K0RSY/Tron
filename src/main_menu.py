from default_inputs import *
from settings import *
from field import *

class MainMenu():
    def cycle(self):
        print(LOGO.strip("\n"))
        print()

        try:
            # Getting field size
            field_size = input("Field size (wdt hgh): ")

            if not field_size:
                field_size = FIELD_SIZE
            else:
                field_size = list(map(int, field_size.split(" ")))

            # Getting FPS
            fps = input("Game speed (fps): ")

            if not fps:
                fps = FPS
            else:
                fps = int(fps)

            # Getting players count
            players_count = input("Player count (cnt): ")

            if not players_count:
                players = PLAYERS.copy()
            else:
                players = []
                for player_index in range(int(players_count)):
                    print()
                    players.append(
                        [
                            int(input(f"Player {player_index + 1}, color (clr:0-{len(COLORS) - 1}): ")),
                            list(map(lambda x: int(x)-1, input(f"Player {player_index + 1}, coordinates (iks:1-{field_size[0]} irg:1-{field_size[1]}): ").split(" "))),
                            input(f"Player {player_index + 1}, direction (drc:u|d|l|r): "),
                            input(f"Player {player_index + 1}, keys (upp lft dwn rgt): ").replace(" ", "")
                        ]
                    )

                    if players[-1][2] not in ["u", "d", "l", "r"]:
                        raise Exception()

            print()
            if input("Press return to play. Type something to exit... "): quit()

            self.field = Field(field_size, players, fps)
            self.field.cycle()
            
        except Exception as e:
            print()
            input("Something went wrong... ")
            print()