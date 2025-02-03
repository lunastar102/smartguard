# SmartGuard

SmartGuard is a Python program designed to track and display detailed task information and system usage statistics. It helps manage Windows resources by providing real-time insights into CPU, memory, disk, and network usage.

## Features

- **CPU Usage Monitoring**: Track the percentage of CPU usage.
- **Memory Usage Monitoring**: Monitor the percentage of memory being used.
- **Disk Usage Monitoring**: Keep an eye on the disk space utilization.
- **Network I/O Tracking**: Display bytes sent and received over the network.
- **Real-Time Display**: Update and display statistics every few seconds.

## Requirements

- Python 3.x
- `psutil` library
- `tabulate` library

## Installation

1. Make sure you have Python 3 installed.
2. Install the required libraries using pip:

   ```bash
   pip install psutil tabulate
   ```

## Usage

1. Clone this repository or download the `smartguard.py` file.
2. Run the program:

   ```bash
   python smartguard.py
   ```

3. The program will start displaying system usage statistics every 5 seconds.
4. To stop the program, press `Ctrl+C`.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Author

SmartGuard is developed by [Your Name].