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
print(calculate_delta(changed_files))
