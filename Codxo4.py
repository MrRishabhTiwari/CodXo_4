import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound  # For Windows sound playing

class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Alarm Clock")
        self.create_widgets()

    def create_widgets(self):
        """Create and place the widgets for the GUI."""
        tk.Label(self.root, text="Set Alarm Time:").pack(pady=10)

        # Frame for time format and time settings
        time_frame = tk.Frame(self.root)
        time_frame.pack(pady=5)

        # Time format dropdown
        self.format_var = tk.StringVar(value='24-hour')
        self.create_dropdown(time_frame, "Format:", self.format_var, ['12-hour', '24-hour'], 0, 1, colspan=2,)

        # Time dropdown lists
        self.hours_var = tk.StringVar(value='00')
        self.minutes_var = tk.StringVar(value='00')
        self.seconds_var = tk.StringVar(value='00')
        self.ampm_var = tk.StringVar(value='AM')  # Default value for 12-hour format

        # Create time dropdowns, positioned in the second row
        self.create_dropdown(time_frame, "Hours:", self.hours_var, range(1, 13), 1, 0)
        self.create_dropdown(time_frame, "Minutes:", self.minutes_var, range(60), 1, 1)
        self.create_dropdown(time_frame, "Seconds:", self.seconds_var, range(60), 1, 2)
        self.create_dropdown(time_frame, "AM/PM:", self.ampm_var, ['AM', 'PM'], 1, 3)

        tk.Button(self.root, text="Set Alarm", command=self.set_alarm).pack(pady=10)
        
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack(pady=10)

        # Initialize AM/PM dropdown visibility
        self.update_ampm_dropdown_visibility()

    def create_dropdown(self, parent, label_text, var, values, row, column, colspan=1):
        """Create a dropdown menu for selecting time values."""
        tk.Label(parent, text=label_text).grid(row=row, column=column*2, padx=5, pady=5, sticky="e")
        options = [f"{value:02d}" if isinstance(value, int) else value for value in values]
        dropdown = tk.OptionMenu(parent, var, *options)
        dropdown.grid(row=row, column=column*2 + 1, padx=5, pady=5, sticky="w", columnspan=colspan)

    def update_ampm_dropdown_visibility(self):
        """Show or hide the AM/PM dropdown based on the selected time format."""
        if self.format_var.get() == '12-hour':
            self.root.children['!frame'].children['!optionmenu'].grid(row=1, column=6, padx=5, pady=5)
        else:
            if 'am/pm' in self.root.children['!frame'].children:
                self.root.children['!frame'].children['!optionmenu'].grid_forget()

    def set_alarm(self):
        """Retrieve alarm time from dropdowns and start the alarm checking thread."""
        hours = self.hours_var.get()
        minutes = self.minutes_var.get()
        seconds = self.seconds_var.get()
        time_format = self.format_var.get()
        ampm = self.ampm_var.get() if time_format == '12-hour' else ''

        if time_format == '12-hour' and hours == '00':
            hours = '12'  # Handle the special case for 12-hour format

        if self.validate_time_format(hours, minutes, seconds, time_format):
            if time_format == '12-hour':
                alarm_time = f"{hours}:{minutes}:{seconds} {ampm}"
            else:
                alarm_time = f"{int(hours):02d}:{minutes}:{seconds}"
                
            threading.Thread(target=self.check_alarm, args=(alarm_time, time_format), daemon=True).start()
            self.status_label.config(text=f"Alarm set for {alarm_time} {time_format}")
        else:
            messagebox.showerror("Invalid Time", "Please enter valid time values.")

    def validate_time_format(self, hours, minutes, seconds, time_format):
        """Validate the time format for hours, minutes, and seconds."""
        try:
            h = int(hours)
            m = int(minutes)
            s = int(seconds)
            if time_format == '12-hour':
                if h == 0:  # 12-hour format uses 1-12 for hours
                    return False
                return 1 <= h <= 12 and 0 <= m < 60 and 0 <= s < 60
            else:
                return 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60
        except ValueError:
            return False

    def check_alarm(self, alarm_time, time_format):
        """Continuously check if the current time matches the alarm time."""
        while True:
            if time_format == '12-hour':
                current_time = time.strftime("%I:%M:%S %p")
            else:
                current_time = time.strftime("%H:%M:%S")
                
            if current_time == alarm_time:
                self.play_alarm_sound()
                messagebox.showinfo("Alarm", "Time to wake up!")
                break
            time.sleep(1)  # Check every second

    def play_alarm_sound(self):
        """Play the alarm sound."""
        try:
            winsound.PlaySound("alarm_sound.wav", winsound.SND_FILENAME)
        except Exception as e:
            print(f"Error playing sound: {e}")

def main():
    """Initialize and run the Tkinter application."""
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
