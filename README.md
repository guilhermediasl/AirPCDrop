# iOS Clipboard Sync

AirPCDrop is a Python script that enables seamless clipboard synchronization between your PC and iOS devices (iPhone or iPad). With this script, you can easily copy content on your PC and use an iOS shortcut to paste it on your iOS device. The script includes a simple HTTP server that runs on your PC and continuously monitors the clipboard for changes.

## Features

- Monitors both text and image content in your PC's clipboard.
- Serves clipboard content over HTTP for easy access from your iOS device.
- Automatically updates the clipboard content as it changes.
- Supports secure content hashing for efficient updates.

## Usage

Follow these steps to set up and use iOS Clipboard Sync:

1. Clone or download this repository to your PC.

2. Ensure you have Python installed on your PC. You can download Python from [python.org](https://www.python.org/downloads/).

3. **Required Python Libraries**: You will also need to install some Python libraries. Open your command prompt or terminal and run the following command to install the required libraries:

   ```bash
   pip install pillow pyperclip

4. Run the Python script `AirPCDrop.py` using the following command:

   ```bash
   python AirPCDrop.py
   ```

   Alternatively, you can run the provided `RUN_AirPCDrop.bat` file to start the script.

5. Once the server is running, you'll see a message indicating that the server is serving at a specific address (e.g., `http://127.0.0.1:8001`). Make note of this address.

6. To copy content to your iOS device, you can use the provided iOS shortcut. You can download and install the shortcut from [here](https://www.icloud.com/shortcuts/c00590f8fc4f4d5c8f24056028efd212).

7. Configure the iOS shortcut to make HTTP requests to the server address mentioned in step 4. You'll need to modify the shortcut to point to your PC's IP address and the correct port number. The shortcut will send a request to your PC, which will retrieve and paste the clipboard content on your iOS device.

8. Enjoy seamless clipboard synchronization between your PC and iOS device!

## Contributing

Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please open an issue or submit a pull request. Your contributions will help make this project even better.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This script is inspired by the need for easy clipboard synchronization between different devices.
- Special thanks to the open-source community for providing libraries and tools that make this project possible.

## Disclaimer

This script is provided as-is and without any warranty. Use it at your own risk.

---

Feel free to further customize this README file with additional information or details as needed.
