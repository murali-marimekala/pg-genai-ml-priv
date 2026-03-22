import json
import copy

# Load the original notebook
with open('wk5_Day2-MMK.ipynb', 'r') as f:
    original_notebook = json.load(f)

# Define split boundaries
# Part 1 (0-21): Random Forest Hyperparameter Tuning
# Part 2 (22-51): Ridge/Lasso/ElasticNet Regularization  
# Part 3 (52-end): KNN Classification

splits = [
    {
        'name': 'wk5_Day2-MMK-1',
        'title': 'Random Forest Hyperparameter Tuning',
        'cells': list(range(0, 22))
    },
    {
        'name': 'wk5_Day2-MMK-2',
        'title': 'Regularization (Ridge, Lasso, ElasticNet)',
        'cells': list(range(22, 52))
    },
    {
        'name': 'wk5_Day2-MMK-3',
        'title': 'K-Nearest Neighbors (KNN)',
        'cells': list(range(52, len(original_notebook['cells'])))
    }
]

# Create separate notebooks
for split in splits:
    new_notebook = copy.deepcopy(original_notebook)
    new_notebook['cells'] = [original_notebook['cells'][i] for i in split['cells']]
    
    # Save new notebook
    filename = f"{split['name']}.ipynb"
    with open(filename, 'w') as f:
        json.dump(new_notebook, f, indent=1)
    
    print(f"✓ Created {filename}")
    print(f"  Topic: {split['title']}")
    print(f"  Cells: {len(split['cells'])}")
    print()

print("Split complete!")
