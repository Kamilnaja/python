from fysom import *

fsm = Fysom(
    {
        "initial": "awake",
        "final": "red",
        "events": [
            {"name": "wakeup", "src": "sleeping", "dst": "awake"},
            {"name": "sleep", "src": "awake", "dst": "sleeping"},
        ],
    }
)
print(fsm.current)
fsm.sleep()
print(fsm.current)
fsm.wakeup()
print(fsm.current)