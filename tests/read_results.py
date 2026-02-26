import sys
import os

def try_read(path):
    encodings = ['utf-16', 'utf-16-le', 'utf-8', 'utf-16-be']
    for enc in encodings:
        try:
            with open(path, 'rb') as f:
                return f.read().decode(enc), enc
        except:
            continue
    return None, None

try:
    content, used_enc = try_read('e2e_results.txt')
    if not content:
        print("Could not read file with any tested encoding.")
        sys.exit(1)
        
    print(f"=== E2E TEST RESULTS (Used: {used_enc}) ===")
    lines = content.split('\n')
    
    # Print summary
    print("\nSUMMARY:")
    print("\n".join(lines[-20:]))
    
    # Search for ANY failure
    print("\nSEARCHING FOR FAILURES...")
    for i, line in enumerate(lines):
        if 'FAIL' in line or 'ERROR' in line:
            print(f"\n--- MATCH AT LINE {i} ---")
            print("\n".join(lines[i-1:i+40]))
            
except Exception as e:
    print(f"Error reading results: {e}")
