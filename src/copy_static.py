import os
import shutil                  # made on the OS easier to copy,move directories etc

def copy_static(src, dst):
    # delete destination if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)

    # recreate destination
    os.mkdir(dst)

    # iterate through source contents
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        # if file -> copy
        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)

        # if directory -> recurse
        else:
            print(f"Entering directory: {src_path}")
            copy_static(src_path, dst_path)