import os

def check_test_folder(test_folder):
    # 1. Check if folder exists
    if not os.path.isdir(test_folder):
        print(f"ERROR: Test folder '{test_folder}' does not exist or is not a directory.")
        return

    # 2. List files
    all_files = os.listdir(test_folder)
    if not all_files:
        print(f"ERROR: Test folder '{test_folder}' is empty (no files).")
        return
    
    recognized_images = []
    unrecognized_files = []
    
    # 3. Valid image extensions your generator expects
    valid_exts = ['jpg', 'jpeg', 'png', 'bmp', 'tif']
    
    # 4. Scan files
    for fname in all_files:
        fpath = os.path.join(test_folder, fname)
        # Skip subfolders or non-files
        if not os.path.isfile(fpath):
            continue
        
        # Check extension
        ext = fname.lower().split('.')[-1]
        if ext in valid_exts:
            recognized_images.append(fname)
        else:
            unrecognized_files.append(fname)

    # 5. Report findings
    if recognized_images:
        print(f"INFO: Found {len(recognized_images)} recognized image file(s) in '{test_folder}':")
        # Print up to 10 sample files
        for im in recognized_images[:10]:
            print("   ", im)
        if len(recognized_images) > 10:
            print(f"   ... (and {len(recognized_images) - 10} more not listed)")
    else:
        print("ERROR: Found no valid images in the test folder (check extensions or file naming).")

    if unrecognized_files:
        print(f"NOTE: {len(unrecognized_files)} file(s) not recognized as valid images:")
        for uf in unrecognized_files[:10]:
            print("   ", uf)
        if len(unrecognized_files) > 10:
            print(f"   ... (and {len(unrecognized_files) - 10} more)")

def debug_test_folder():
    # Replace with the actual path to your test folder
    test_folder = r"Not augmented\\testing_data"
    check_test_folder(test_folder)

if __name__ == "__main__":
    debug_test_folder()
