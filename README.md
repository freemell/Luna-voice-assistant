
# Luna - AI Assistant

Luna is a voice-controlled AI assistant developed using Python, PyQt5, and several other libraries to help with various tasks such as checking the time, weather, opening applications, sending emails, searching the web, playing music, and more. Luna listens to voice commands and responds with spoken output, allowing users to interact naturally.

## Features

- **Voice-controlled AI**: Luna listens to commands and executes them.
- **Graphical User Interface**: Built using PyQt5, Luna provides an interactive GUI with animated elements.
- **Task Automation**: Open applications, fetch the weather, tell the time, perform Google searches, and more.
- **Email Sending**: Send emails through voice commands.
- **News Updates**: Get the latest news headlines.
- **Music Player**: Play music directly from your device.
- **Screenshot Capturing**: Capture and save screenshots.
- **Jokes and Fun**: Get jokes or interact with Luna casually.

## Requirements

The project depends on several Python libraries. You can install the required packages using the `requirements.txt` file:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

Key dependencies include:
- PyQt5
- PyAutoGUI
- PyWhatKit
- WolframAlpha API
- BeautifulSoup
- Requests

## Installation

1. Clone the repository to your local machine.
2. Install the required Python packages by running:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`
3. Make sure you have `pyqt5_plugins` compatible with your Python version. If required, install the appropriate wheel package for your system:
   \`\`\`bash
   pip install pyqt5_plugins-5.15.9.2.3-cp311-cp311-win_amd64.whl
   \`\`\`

## Usage

1. Run the `main.py` file to start Luna.
   \`\`\`bash
   python main.py
   \`\`\`
2. Luna will initialize and show a graphical user interface.
3. Interact with Luna by typing commands in the text box or by speaking commands directly.

## File Structure

- `main.py`: Main application file that initializes and runs Luna.
- `ui_main_window.py`: GUI layout file generated using PyQt5. Contains the structure of the main window, buttons, labels, and command input fields.
- `requirements.txt`: List of Python packages required for the project.

## Example Commands

- "What’s the time?"
- "What’s the weather in London?"
- "Open Google"
- "Send an email"
- "Play music"
- "Take a screenshot"

## Future Enhancements

- Voice-based note-taking.
- Integration with additional APIs for expanded functionality.
- Improved voice recognition accuracy.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
"# Luna-voice-assistant" 
"# Luna-voice-assistant" 
