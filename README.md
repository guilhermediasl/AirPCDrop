# AirPCDrop
PC - iOS Clipboard Local network Sync 

iOS Clipboard Sync
AirPCDrop is a Python script that enables seamless clipboard synchronization between your PC and iOS devices (iPhone or iPad). With this script, you can easily copy content on your PC and use an iOS shortcut to paste it on your iOS device. The script includes a simple HTTP server that runs on your PC and continuously monitors the clipboard for changes.

Features
Monitors both text and image content in your PC's clipboard.
Serves clipboard content over HTTP for easy access from your iOS device.
Automatically updates the clipboard content as it changes.
Supports secure content hashing for efficient updates.
Usage
Follow these steps to set up and use iOS Clipboard Sync:

Clone or download this repository to your PC.

Run the Python script clipboard_sync.py on your PC. This script will start an HTTP server that serves clipboard content.

bash
Copy code
python clipboard_sync.py
Once the server is running, you can use an iOS shortcut or make HTTP requests to access the clipboard content from your iOS device.

Enjoy seamless clipboard synchronization between your PC and iOS device!

Contributing
Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please open an issue or submit a pull request. Your contributions will help make this project even better.

License
This project is licensed under the MIT License.

Acknowledgments
This script is inspired by the need for easy clipboard synchronization between different devices.
Special thanks to the open-source community for providing libraries and tools that make this project possible.
Disclaimer
This script is provided as-is and without any warranty. Use it at your own risk.
