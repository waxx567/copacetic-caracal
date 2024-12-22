# Voice Recognition Bot

This project is a voice recognition bot built using Python. It records audio from the user, processes the recorded file using Google Speech Recognition, and saves the transcribed text to a file.

## Features

- Record audio from the user's microphone.
- Play back the recorded audio.
- Recognize and transcribe speech using Google Speech Recognition.
- Save the transcribed text to a text file.

## Requirements

The following Python libraries are required:

- `speech_recognition` - for speech-to-text processing
- `sounddevice` - for recording and playing audio
- `numpy` - for audio data handling
- `scipy` - for saving audio to a .wav file

To install these packages, run:

```bash
pip install speechrecognition sounddevice numpy scipy
```

## How to Use

1. Clone the repository.
2. Install the required libraries.
3. Run the bot using:

```bash
python your_script_name.py
```

4. Speak into the microphone when prompted.
5. The audio will be recorded, played back, and transcribed.
6. The transcribed text will be saved in `VOICE.txt`.

## File Descriptions

- `your_script_name.py`: Main program file.
- `over-radio-countdown_108bpm_A_minor.wav`: Test audio file (not required for normal operation).
- `RECORDING.wav`: Temporary file for storing the user's audio recording.
- `VOICE.txt`: Output file containing the transcribed text.

## How It Works

1. **Audio Recording**: The bot records a 5-second audio clip using the microphone.
2. **Audio Playback**: The bot plays back the recorded audio for confirmation.
3. **Speech Recognition**: It processes the recorded audio using Google Speech Recognition.
4. **Text Saving**: The recognized text is saved into `VOICE.txt`.

## Limitations

- Requires an active internet connection for Google Speech Recognition.
- Works best in a quiet environment.

## License

This project is licensed under the MIT License.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

## Acknowledgments

- Internet Made Coder: [Video](https://youtu.be/ZRlbf5P2iMA?si=BAa_5NoPUCN5D6c1)

---

Thank you for using the Voice Recognition Bot!

