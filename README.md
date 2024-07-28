# CodXo_4
# Simple Tkinter Alarm Clock

This is a basic alarm clock application built using Python's `tkinter` library. It features a graphical user interface (GUI) where you can set an alarm time, and when the alarm goes off, it displays a message and plays a sound.

## Features

- **Set Alarm Time:** Enter the time in `HH:MM:SS` format.
- **Alarm Notification:** Displays a popup message when the alarm time is reached.
- **Sound Alert:** Plays an alarm sound when the time matches the set alarm time.

## Requirements

- Python 3.x
- `tkinter` (comes with Python standard library)
- `winsound` (for Windows users)

## Setup

### Prerequisites

Ensure you have Python 3.x installed on your system. The `tkinter` and `winsound` libraries are included with Python, so no additional installation is required.

### Install Python (if not already installed)

- **Windows/macOS/Linux:** Follow the [official Python installation guide](https://www.python.org/downloads/) for your operating system.

### Prepare the Alarm Sound

1. Save your alarm sound file as `alarm_sound.wav`.
2. Place `alarm_sound.wav` in the same directory as your script, or modify the path in the script if you place it elsewhere.

## How to Use
1. **Run the Application:**

   Open a terminal or command prompt, navigate to the directory where the script is located, and run:

   ```bash
   python Codxo4.py
   ```

2. **Set the Alarm:**

   - Enter the desired alarm time in the format `HH:MM:SS` (e.g., `07:30:00` for 7:30 AM).
   - Click the "Set Alarm" button.

   When the current time matches the set alarm time, a popup will appear with an alert message, and the sound will play.

## Code Explanation

- **Imports:** Uses `tkinter` for GUI, `messagebox` for notifications, `time` for time functions, `threading` to check the alarm in the background, and `winsound` to play the sound on Windows.
- **Functions:**
  - `set_alarm()`: Retrieves and validates the alarm time, and starts a background thread to monitor it.
  - `check_alarm()`: Continuously checks if the current time matches the alarm time and triggers the alarm.
  - `play_alarm_sound()`: Plays the alarm sound using `winsound`.
- **GUI Elements:** Includes a label, entry field, button, and status label.

## Compatibility

- **Windows:** Fully supported with `winsound` for sound playback.
- **macOS/Linux:** You may need to modify the `play_alarm_sound()` function to use a different sound playback method if `winsound` is not available.

## Troubleshooting

- **Sound Playback Issues:** Ensure the `alarm_sound.wav` file is correctly placed and accessible. Verify that your system supports sound playback commands.
- **Invalid Time Format:** Make sure you enter the time in the `HH:MM:SS` format.
