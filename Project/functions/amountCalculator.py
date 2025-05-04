import os
import glob
import csv
import json

def countSubs(subLimit):
    # Set the folder path
    folder_path = "storage"

    # Get all CSV files in the storage folder
    csv_files = glob.glob(os.path.join(folder_path + "/secondarySubs", "*.csv"))

    totalSubsPerChannel = {}

    file_count = 0

    for file in csv_files:
        #print(os.path.basename(file)) 

            # Count rows first
        with open(file, mode="r", newline="", encoding="utf-8") as f:
            total_rows = sum(1 for row in csv.reader(f) if row)
        #print(f"Total rows in this file before processing: {total_rows}")

        if int(total_rows) <= int(subLimit):
            with open(file, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row:  # Ensure the row is not empty
                        if row[1] in totalSubsPerChannel:
                            totalSubsPerChannel[row[1]][1] += 1
                        else:
                            totalSubsPerChannel[row[1]] = [row[0], 1]

        file_count += 1

        # For testing

        #if file_count == 5:
            #print(totalSubsPerChannel) 
        #    break  

    # Define the JSON file path
    json_file_path = os.path.join(folder_path + "/totalSubs", "totalSubsPerChannel.json")

    # Write the dictionary to a JSON file
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(totalSubsPerChannel, json_file, indent=4, ensure_ascii=False)

    #print(f"Data successfully written to {json_file_path}")
