
import board

from kmk.modules.encoder import EncoderHandler
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros, UnicodeModeWinC
from kmk.scanners import DiodeOrientation

# Define the modules
keyboard = KMKKeyboard()
macros = Macros(unicode_mode=UnicodeModeWinC)
encoder = EncoderHandler()
keyboard.modules.append(macros, encoder)
# Define the keys pins
keyboard.col_pins = (board.GP29, board.GP1, board.GP2)
keyboard.row_pins = (board.GP3, board.GP4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
# Define the encoder pins
encoder.pins = (board.GP27, board.GP28, None)
# Define the macros
Copy = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.C),
    Release(KC.LCTL)
)

Paste = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.V),
    Release(KC.LCTL)
)

Pscreen = KC.MACRO(
    Press(KC.LWIN),
    Tap(KC.PSCREEN),
    Release(KC.LWIN)
)

Cutscr = KC.MACRO(
    Press(KC.LWIN, KC.LSHIFT),
    Tap(KC.S),
    Release(KC.LWIN, KC.LSHIFT)
)

# Define the encoder actions
encoder.map = (KC.VOLD, KC.VOLU, KC.NO)

keyboard.keymap = [
    [Copy , KC.MUTE , Pscreen],
    [Paste , KC.N , Cutscr],
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()