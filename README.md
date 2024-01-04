
# Proxy Fetcher

Proxy Fetcher is a Python package designed to efficiently fetch and test proxies. It automatically retrieves proxy addresses from free-proxy-list.net and tests them to find the ones that work with your specified URL.

## Setup and Run Script

### 1. Create a Virtual Environment

It's recommended to create a virtual environment to avoid conflicts with other Python packages.

```bash
python3 -m venv env
```

### 2. Activate the Virtual Environment

Activate the virtual environment to work with isolated package dependencies.

- **Windows:**
```bash
.\env\Scripts\activate
```

- **Mac/Linux:**
```bash
source env/bin/activate
```

### 3. Install Required Packages

Install the required packages within the virtual environment.

```bash
pip install -r requirements.txt
```

### 4. Run the Script

To run the script and start fetching proxies, execute the following:

```bash
python3 -m ProxyFetcher.ProxyFetcher
```

## Executing the Package

To fetch proxies with the desired URL, number of proxies, and threads, use:

```python
from ProxyFetcher.ProxyFetcher import fetch_with_proxies
response = fetch_with_proxies('http://httpbin.org/ip', 10, 4)
if response:
    print(f"Successfully fetched with proxy: {response.text}")
else:
    print("Failed to fetch with any of the proxies.")
```

### Function Parameters:

- `url`: The target URL to fetch using the proxies.
- `num_of_proxies`: The number of proxy addresses to fetch and test.
- `num_threads`: The number of threads to use for concurrent testing of proxies.

## Install as Pip Package

You can install this package via pip directly from the GitHub repository using:

```bash
pip install git+https://github.com/freekvlier/python-proxy-fetcher.git
```

Or, for a local installation from the source code, navigate to the directory containing `setup.py` and run:

```bash
pip install .
```

## Optional Maintenance

- **Update Requirements:** 
To update the `requirements.txt` file, run:

```bash
pip freeze > requirements.txt
```

- **Uninstall Package:**
To remove the package, execute:

```bash
pip uninstall ProxyFetcher
```

## Note

This package is intended for educational purposes and should be used responsibly. Ensure you comply with the terms of service for any platforms you interact with using this tool.

---
