# Tehran Taxi Price Comparison

This project automates the process of collecting taxi fare data for two different ride-hailing services in Tehran, Iran, over a 24-hour period. The services compared are Snapp and Tapsi. The goal is to gather data on the prices for a specific route and analyze the variation in prices over time, as well as how these prices correlate with traffic conditions.

## Project Overview

The project collects fare data for the following route:
- **From**: Azadi Square, Tehran
- **To**: Madar Square, Mirdamad Boulevard, Tehran

### Components
1. **Snapp Price Collection Script**: A Python script that uses Selenium to interact with Snapp's web application, collects fare prices at regular intervals, and saves the data to a JSON file.
2. **Tapsi Price Collection Script**: A Python script that uses Selenium to interact with Tapsi's web application, collects fare prices at regular intervals, and saves the data to a JSON file.
3. **Traffic Data Collection**: Traffic data is collected and used to analyze its impact on fare prices.
4. **Data Visualization**: The collected data is visualized using matplotlib to compare fare prices and traffic conditions over time.



## Files and Directories

- **result/**: Directory containing the final results and plots.
  - `final_data.xlsx`: Excel file with the final compiled data.
  - `final_PLOT_data.xlsx`: Excel file with the data used for plotting.
  - `final_plot.png`: Image file of the final plot.

- **Snapp_DATA/**: Directory containing data related to Snapp.
  - `snapp_data_Merged.xlsx`: Excel file with merged Snapp data.
  - `snapp_data.xlsx`: Excel file with Snapp data.
  - `snapp1.json`: JSON file with Snapp data.
  - `Snapp2.txt`: Text file with Snapp data.

- **Tapsi_DATA/**: Directory containing data related to Tapsi.
  - `4.txt`: Text file with Tapsi data.
  - `tapsi_data_merged.xlsx`: Excel file with merged Tapsi data.
  - `tapsi_data.xlsx`: Excel file with Tapsi data.
  - `tapsi1.json`: JSON file with Tapsi data.
  - `tapsi2.5.json`: JSON file with Tapsi data.
  - `tapsi2.txt`: Text file with Tapsi data.
  - `tapsi3.json`: JSON file with Tapsi data.
  - `tapsi3.txt`: Text file with Tapsi data.

- **chromedriver.exe**: Executable for ChromeDriver, used by Selenium to automate web browser interactions.

- **preprocessing_data.ipynb**: Jupyter notebook for data preprocessing.

- **Snapp.py**: Python script for collecting Snapp price data.

- **Tapsi.py**: Python script for collecting Tapsi price data.

- **README.md**: Project documentation file (this file).

- **requirements.txt**: List of Python packages required for the project.

This structure helps to organize and manage the project files effectively, ensuring that related files are grouped together and easy to locate.

## Getting Started

### Prerequisites

- Python 3.7+
- Google Chrome browser
- ChromeDriver (ensure compatibility with your Chrome version)
- Selenium library for Python

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/aminmoghadasi75/Snapp-Tapsi.git
    cd tehran-taxi-price-comparison
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up ChromeDriver**:
   Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in an appropriate directory. Update the path to ChromeDriver in the scripts if necessary.

### Running the Scripts

1. **Run the Snapp price collection script**:
    ```bash
    python Snapp.py
    ```

2. **Run the Tapsi price collection script**:
    ```bash
    python Tapsi.py
    ```

3. **Run the data visualization script**:
    ```bash
    python visualize_data.py
    ```

### Collecting Prices

- The scripts will prompt for necessary inputs like phone number and verification codes.
- Data will be collected at regular intervals for 24 hours and saved to respective JSON files.

### Visualizing Data

- The `visualize_data.py` script will generate plots comparing fare prices and traffic conditions over time.

---

By following these steps, you can collect and visualize taxi fare data for Snapp and Tapsi, helping to analyze price trends and their correlation with traffic conditions.
# Snapp-Tapsi
