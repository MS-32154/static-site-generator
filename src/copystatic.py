import os
import shutil


def copy_files_recursive(src_dir, dist_dir):
    if not os.path.exists(dist_dir):
        os.mkdir(dist_dir)

    for element in os.listdir(src_dir):
        src_path = os.path.join(src_dir, element)
        dist_path = os.path.join(dist_dir, element)
        print(f" * {src_path} -> {dist_path}")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dist_path)

        else:
            copy_files_recursive(src_path, dist_path)


if __name__ == "__main__":
    copy_files_recursive("static", "public")
