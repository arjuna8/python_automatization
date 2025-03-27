import pandas as pd
from thefuzz import process


# Function to read Excel files
def read_excel(file_path, column_name):
    """
    Reads an Excel file and returns a list of values from a specified column.
    """
    df = pd.read_excel(file_path)
    return df[column_name].dropna().tolist()


# Function to perform fuzzy matching
def fuzzy_match(requests, source_data, limit=5):
    """
    Matches each request against the source data using fuzzy matching.
    Returns the top matches for each request.
    """
    results = []
    for request in requests:
        matches = process.extract(request, source_data, limit=limit)
        results.append((request, matches))
    return results


# Main function
def main():
    # File paths (update with your actual file paths)
    requests_file = "/home/michaelfoucault/Downloads/requests_pavement_fuzzysearch.xlsx"  # File containing requests
    source_file = "/home/michaelfoucault/Downloads/data_source_pavement_fuzzysearch.xlsx"  # File containing source data

    # Column names in the Excel files
    requests_column = "Requests"  # Column name in requests file
    source_column = "SourceData"  # Column name in source data file

    # Read data from Excel files
    print("Reading data from Excel files...")
    requests = read_excel(requests_file, requests_column)
    source_data = read_excel(source_file, source_column)

    # Perform fuzzy matching
    print("Performing fuzzy matching...")
    matches = fuzzy_match(requests, source_data)

    # Save results to a new Excel file
    print("Saving results to 'fuzzy_matches.xlsx'...")
    with pd.ExcelWriter("fuzzy_matches.xlsx") as writer:
        for request, match_list in matches:
            match_df = pd.DataFrame(match_list, columns=["Matched String", "Score"])
            match_df.insert(0, "Request", request)  # Add the original request for context
            match_df.to_excel(writer, sheet_name=request[:30], index=False)  # Limit sheet name to 30 characters


if __name__ == "__main__":
    main()
