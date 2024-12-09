import pandas as pd
from thefuzz import process
import os

survey = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'restaurants_L2_dirty.csv'))
print(survey.info())
categories = pd.DataFrame({
    'type': ['California', 'New York']
})

# For each correct category
for state in categories['type']:
    # Find potential matches in states with typos
    matches = process.extract(state, survey['type'], limit=survey.shape[0])
    # For each potential match
    for potential_match in matches:
        # If high similarity score
        if potential_match[1] >= 80:
            # Replace typo with correct category
            survey.loc[survey['type'] == potential_match[0], 'type'] = type
            
# Print categories to verify mapping
print(survey['type'].unique())
