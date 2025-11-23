import os
import requests

urls = {
    "isone_load-ard-nat_hr_2021.csv": "https://www.eia.gov/electricity/wholesalemarkets/csv/isone_load-ard-nat_hr_2021.csv",
    "isone_load-ard-nat_hr_2022.csv": "https://www.eia.gov/electricity/wholesalemarkets/csv/isone_load-ard-nat_hr_2022.csv",
    "isone_load-ard-nat_hr_2023.csv": "https://www.eia.gov/electricity/wholesalemarkets/csv/isone_load-ard-nat_hr_2023.csv",
    "isone_load-ard-nat_hr_2024.csv": "https://www.eia.gov/electricity/wholesalemarkets/csv/isone_load-ard-nat_hr_2024.csv",
    "isone_load-ard-nat_hr_2025.csv": "https://www.eia.gov/electricity/wholesalemarkets/csv/isone_load-ard-nat_hr_2025.csv",
}

def main():
    # Folder where THIS script lives: .../iso-ne-load-forecasting/data
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # We want .../iso-ne-load-forecasting/data/raw
    raw_dir = os.path.join(script_dir, "raw")
    os.makedirs(raw_dir, exist_ok=True)

    for filename, url in urls.items():
        print(f"Downloading {filename}...")
        r = requests.get(url)
        r.raise_for_status()  # will error if download fails

        filepath = os.path.join(raw_dir, filename)
        with open(filepath, "wb") as f:
            f.write(r.content)

        print(f"  → Saved to {filepath}")

    print("\nDone — files saved to data/raw/")

if __name__ == "__main__":
    main()
