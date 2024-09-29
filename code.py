print("starting")

import board  # type: ignore
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from storage import getmount

XXXXXXX = KC.NO

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11)
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

if str(getmount("/").label)[-1].upper() == "L":
    keyboard.keymap = [
        # fmt: off
        [ 
            KC.ESC,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,
            KC.TAB,     KC.Q,       KC.E,       KC.R,       KC.T,       KC.L,
            KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,
            KC.SHIFT,   KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,
            KC.LCTRL,   KC.LGUI,    KC.LALT,    XXXXXXX,    XXXXXXX,    KC.SPACE,
        ],
        # fmt: on
    ]
else:
    keyboard.keymap = [
        # fmt: off
        [
            KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.BSPC,
            KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSLS,
            KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.ENTER,
            KC.N,       KC.M,       KC.COMMA,   KC.DOT,     KC.N0,      KC.BSPC,
            KC.SPACE,   KC.RALT,    KC.RCTRL,   XXXXXXX,    XXXXXXX,    XXXXXXX,
        ],
        # fmt: on
    ]

if __name__ == "__main__":
    keyboard.go()
