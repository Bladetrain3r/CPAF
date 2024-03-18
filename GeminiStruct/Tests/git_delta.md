Certainly! Let's create a simple example using Python to interact with a Git repository and measure the delta between `HEAD` and `HEAD-1`. This example will involve three steps: setting up the repository with sample text files, making modifications, and then using a Python script to calculate the deltas for each file.

### Step 1: Setting Up the Git Repository

First, ensure you have Git installed on your system. You can check by running `git --version` in your terminal. If Git is not installed, follow the installation instructions from the [official Git website](https://git-scm.com/).

1. **Initialize a New Git Repository**:
   ```bash
   mkdir my_sample_repo
   cd my_sample_repo
   git init
   ```

2. **Create Three Text Files** and make the initial commit:
   ```bash
   echo "This is file 1." > file1.txt
   echo "This is file 2." > file2.txt
   echo "This is file 3." > file3.txt
   git add .
   git commit -m "Initial commit: Added 3 files."
   ```

### Step 2: Modify the Text Files and Commit Changes

Make some changes to the text files to simulate development activity:

1. **Modify the Files**:
   ```bash
   echo "Modified line in file 1." > file1.txt
   echo "Another new line in file 2." >> file2.txt
   # Leave file3.txt unchanged for this example
   ```

2. **Commit the Changes**:
   ```bash
   git add .
   git commit -m "Second commit: Modified files."
   ```

### Step 3: Python Script to Calculate Delta Between `HEAD` and `HEAD-1`

Now, let's write a Python script to calculate the delta. This script uses the `git diff` command to find differences between the last two commits for each file.

```python
import subprocess

# Function to get the list of changed files between HEAD and HEAD-1
def get_changed_files():
    cmd = ['git', 'diff', '--name-only', 'HEAD', 'HEAD~1']
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip().split('\n')

# Function to calculate the delta for each changed file
def calculate_delta(files):
    for file in files:
        if file:  # Check if filename is not empty
            print(f"\nCalculating delta for: {file}")
            cmd = ['git', 'diff', '--unified=0', 'HEAD', 'HEAD~1', '--', file]
            result = subprocess.run(cmd, stdout=subprocess.PIPE)
            print(result.stdout.decode('utf-8'))

# Main Execution
changed_files = get_changed_files()
calculate_delta(changed_files)
```

This script:
- Retrieves the names of files changed between the last two commits.
- For each changed file, it runs `git diff` to display the differences, using `--unified=0` to minimize context around changes, making it easier to focus on the deltas.

### Instructions for Running the Script

1. Ensure Python is installed on your system.
2. Save the Python script to a file (e.g., `calculate_delta.py`) in the root of your Git repository.
3. Run the script using Python:
   ```bash
   python calculate_delta.py
   ```

The script will output the changes (deltas) for each file that was modified between the last two commits. This method provides a straightforward way to quantify changes in text files in a Git repository, reflecting the system's evolution over time.