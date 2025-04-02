# Remote Voice Assistant for PC

This project allows users to control their PC remotely using voice commands through an Android application. It consists of two main components:

1. **Android Application (`VoiceAssistantAndroid`)**: Captures voice commands from the user and transmits them to the PC.
2. **Python Server (`VoiceAssistantPython`)**: Runs on the PC, receives commands from the Android app, and executes the corresponding actions.

## Features

- **Remote Control**: Operate your PC using voice commands from your Android device.
- **Cross-Platform Communication**: Seamless interaction between Android and PC components.
- **Extensible Commands**: Easily add new voice commands and corresponding PC actions.

## Getting Started

### Prerequisites

- **Android Device**: Running Android OS to install the `VoiceAssistantAndroid` app.
- **PC**: Running Windows, Linux, or macOS with Python installed.
- **Network Connection**: Both devices should be connected to the same network.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Dhruvdangi03/Remote-Voice-assistant-for-PC.git
   ```


2. **Set Up the Python Server**:

   - Navigate to the `VoiceAssistantPython` directory:

     ```bash
     cd Remote-Voice-assistant-for-PC/VoiceAssistantPython
     ```

   - Install required Python packages:

     ```bash
     pip install -r requirements.txt
     ```

   - Run the server:

     ```bash
     python main.py
     ```

3. **Install the Android Application**:

   - Navigate to the `VoiceAssistantAndroid` directory.
   - Open the project in Android Studio.
   - Build and install the app on your Android device.

## Usage

1. **Start the Python Server**: Ensure the server is running on your PC.
2. **Connect the Android App**: Open the app and enter the IP address of your PC.
3. **Issue Voice Commands**: Use the app to send voice commands to the PC.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
