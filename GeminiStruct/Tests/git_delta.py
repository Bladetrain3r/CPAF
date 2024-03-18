import subprocess

# Function to get the list of changed files between HEAD and HEAD-1
def get_changed_files():
    cmd = ['git', 'diff', '--name-only', 'HEAD', 'HEAD~1']
    result = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
    files = result.stdout.decode('utf-8').strip().split('\n')
    return [file for file in files if file]  # Filter out empty filenames

def calculate_delta(files):
    for file in files:
        print(f"\nCalculating delta for: {file}")
        cmd = ['git', 'diff', '--unified=0', 'HEAD', 'HEAD~1', '--', file]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
        diff_lines = result.stdout.decode('utf-8').split('\n')
        
        # Count the added (+) and removed (-) lines
        added = sum(1 for line in diff_lines if line.startswith('+') and not line.startswith('+++'))
        removed = sum(1 for line in diff_lines if line.startswith('-') and not line.startswith('---'))
        
        # Define delta as the sum of added and removed lines
        delta = added + removed
        print(f"Delta for {file}: {delta} (Added lines: {added}, Removed lines: {removed})")

# Main Execution
changed_files = get_changed_files()
if changed_files:
    calculate_delta(changed_files)
else:
    print("No files changed between HEAD and HEAD~1.")
