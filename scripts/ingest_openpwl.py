import shutil
import pandas
import subprocess
import os

def download_openpwl_data(output_loc, repo_loc):
    """
    Download and build the most recent OpenPowerlifting data from a git repository.

    Parameters:
    - output_loc: The location where the downloaded data will be stored.
    - repo_loc: The location of the git repository.

    Returns:
    None
    """
    repo_url = "https://gitlab.com/openpowerlifting/opl-data.git"
    
    if is_git_repo(repo_loc) and get_git_repo_name(repo_loc) == 'opl-data':
        try:
            subprocess.run(["git", "config", "--global", "pull.rebase", "true"], check=True)
            result = subprocess.run(["git", "-C", repo_loc, "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                print("Git pull successful")
                print(f"Output: {result.stdout}")
            else:
                print("Git pull failed")
                print(f"Error: {result.stderr}")
        except Exception as e:
            print("Error executing git pull:", e)
    else: 
        try:      
            result = subprocess.run(["git", "clone", repo_url, repo_loc], check=True)
            if result.returncode == 0:
                print("Git clone successful")
                print(f"Output: {result.stdout}")
            else:
                print("Git clone failed")
                print(f"Error: {result.stderr}")
        except Exception as e:
            print("Error executing git clone:", e)     

    subprocess.run(["tests/check", "--compile"], cwd=repo_loc, check=True)

    shutil.copytree(f"{repo_loc}/build", output_loc, dirs_exist_ok=True)

def is_git_repo(path):
    """
    Check if a given path is a valid git repository.

    Parameters:
    - path: The path to check.

    Returns:
    - True if the path is a git repository, False otherwise.
    """
    if not os.path.exists(path):
        return False

    try:
        subprocess.run(["git", "-C", path, "rev-parse", "--is-inside-work-tree"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    
def get_git_repo_name(path):
    """
    Get the name of the git repository from a given path.

    Parameters:
    - path: The path to the git repository.

    Returns:
    - The name of the git repository, or None if the path is not a valid git repository.
    """
    if not os.path.exists(path):
        return None

    try:
        subprocess.run(["git", "-C", path, "rev-parse", "--is-inside-work-tree"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError:
        return None

    remote_url = subprocess.run(["git", "-C", path, "config", "--get", "remote.origin.url"],
                                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, check=True)

    repo_name = os.path.splitext(os.path.basename(remote_url.stdout.strip()))[0]
    return repo_name

def transform_bulk_csv(inpath, outpath):
    """
    Transform the OpenPowerlifting human bulk CSV into a partitioned parquet file.

    Parameters:
    - inpath: The path to the input CSV file.
    - outpath: The path to save the output parquet file.

    Returns:
    None
    """
    df = pandas.read_csv(inpath)
    df.to_parquet(outpath)

    return None
