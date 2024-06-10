import pandas as pd
import json
import math

# Load the Excel file
df = pd.read_excel('Toolbox mapping.xlsx')

# Function to handle NaN values
def handle_nan(value):
    return "" if (isinstance(value, float) and math.isnan(value)) else value

# Function to convert a row to the desired JSON format
def convert_row_to_json(row):
    return {
        "tool_name": handle_nan(row.get("Tool name", "")),
        "tool_summary": handle_nan(row.get("Tool summary", "")),
        "url_to_tool": handle_nan(row.get("Link to tool", "")),
        "publications": [
            {"publication": handle_nan(row.get("Publication Link ", ""))},
            {"publication": handle_nan(row.get("Publication link 2", ""))},
            {"publication": handle_nan(row.get("Publication link 3", ""))}
        ],
        "last_updated": handle_nan(row.get("Last updated", "")),
        "tool_type": {
            "guidance": row.get("Guidance", "") == "X",
            "software": row.get("Software", "") == "X"
        },
        "review_families": {
            "systematic": row.get("Systematic", "") == "X",
            "rapid": row.get("Rapid ", "") == "X",
            "qualitative": row.get("Qualitative", "") == "X",
            "scoping": row.get("Scoping", "") == "X",
            "mapping": row.get("Mapping", "") == "X",
            "mixed_method": row.get("Mixed Methods", "") == "X",
            "review_of_reviews": row.get("Reviews of reviews", "") == "X",
            "other": row.get("Other", "") == "X"
        },
        "review_stages": {
            "multiple_review": row.get("Multiple", "") == "X",
            "protocol": row.get("Protocol", "") == "X",
            "search": row.get("Search", "") == "X",
            "screen": row.get("Screening", "") == "X",
            "data_extract": row.get("Data extraction", "") == "X",
            "quality_assess": row.get("Quality assessment", "") == "X",
            "synthesis": row.get("Synthesis", "") == "X",
            "report": row.get("Report", "") == "X",
            "reference_management": row.get("Reference management", "") == "X",
            "stakeholder_engagement": row.get("Stakeholder engagement", "") == "X"
        },
        "cost_info": {
            "free": row.get("Free", "") == "X",
            "free_version_available": row.get("Free version available", "") == "X",
            "free_trial": row.get("Free trial", "") == "X",
            "payment_required": row.get("Payment required", "") == "X",
            "open_source": row.get("Open access", "") == "X"
        },
        "date_added": handle_nan(row.get("Added to SR Toolbox", ""))
    }

# Apply the function to each row in the dataframe
tools_json = df.apply(convert_row_to_json, axis=1).tolist()

# Save the list of dictionaries to a JSON file
with open('tools.json', 'w') as json_file:
    json.dump(tools_json, json_file, indent=4)

print("Conversion complete. JSON file saved as 'tools.json'.")