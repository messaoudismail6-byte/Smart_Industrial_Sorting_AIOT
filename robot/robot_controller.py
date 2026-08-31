"""
Generic robot state-machine adapter.
Replace send_command() with the API/SDK of the actual robot.
"""

import time
from enum import Enum

class State(Enum):
    IDLE = 0
    PICK = 1
    PLACE = 2
    DONE = 3

class RobotController:
    def __init__(self):
        self.state = State.IDLE
        self.ready = True

    def send_command(self, command: str):
        print(f"[ROBOT] {command}")

    def cycle(self, target: str):
        if not self.ready:
            raise RuntimeError("Robot not ready")

        self.state = State.PICK
        self.send_command("PICK")
        time.sleep(0.3)

        self.state = State.PLACE
        self.send_command(f"PLACE_{target}")
        time.sleep(0.3)

        self.state = State.DONE
        self.send_command("DONE")
        self.state = State.IDLE

if __name__ == "__main__":
    RobotController().cycle("B")
