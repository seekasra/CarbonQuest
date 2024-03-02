![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![PyQt5](https://img.shields.io/badge/uses-PyQt5-green.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)


# CarbonQuest: Visualizing Great Britain's Electrical Carbon Footprint

CarbonQuest is an advanced, PyQt5-based desktop application designed to interact directly with the Official Carbon Intensity API for Great Britain, developed by National Grid. This tool provides a real-time and historical perspective on the carbon intensity of electricity consumed within Great Britain, offering an educational insight into the environmental impact of energy usage. Users can access carbon intensity forecasts, actual intensity data, and factors for various fuel types, all visualized through engaging graphical representations. Learn more about carbon intensity at [carbonintensity.org.uk](https://carbonintensity.org.uk).

## Key Features

- **Real-Time Data Access**: Fetch and display carbon intensity data for the current half-hour.
- **Forecast Visualization**: View carbon intensity forecasts for today and any specific date.
- **Fuel Type Analysis**: Access carbon intensity factors for each fuel type, understanding their environmental impact.
- **Data Visualization**: Visualize carbon intensity data through interactive graphs, making complex data easily understandable.

## Prerequisites

Before installing CarbonQuest, ensure your system meets the following requirements:
- Python 3.6 or higher
- Pip for Python package management

## Installation Guide

Follow these steps to install CarbonQuest on your system:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/carbonquest.git
   ```
2. Navigate to the project directory:
   ```sh
   cd carbonquest
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## How to Use CarbonQuest

Execute the following command within the project's root directory to launch CarbonQuest:
```bash
python carbon_insight_app.py
```
Upon launching, the application presents a user-friendly GUI. Utilize the buttons to perform actions such as fetching current carbon intensity, viewing today's forecast, accessing fuel type factors, and fetching data for a specific date. The application's graphical area displays the data and trends, offering a visual representation of Great Britain's carbon footprint.

## Contribution Guidelines

Contributions to CarbonQuest are highly encouraged. If you have improvements or suggestions, please fork the repository, make your changes, and submit a pull request. You can also open an issue with the tag "enhancement" to discuss potential changes. We appreciate your input in making CarbonQuest a more informative and useful tool.

## Support and Questions

For support or to report issues, please open an issue on the GitHub repository page.

## Licensing

CarbonQuest is made available under the [MIT License](LICENSE.md). For more details, see the LICENSE file in the project repository.
