import shutil
import pandas
import subprocess
import os

# This script will ingest data from the OpenPowerlifting repo.

# TODO
    # Choose between getting data from repo or just getting the CSV that they provide
        # getting data from repo will allow for lifter-data as well
    # implementation
        # Just clone the repo and regularly pull to update the contents
            # Once we pull how do we update the transformations


# the downloaded CSV has the revision number at the end

def download_openpwl_data(output_loc, repo_loc):

    # Download and build most recent OpenPowerlifting data
        # Parameters
            # git repo location. could be s3 location, local, or none
            # output location

    repo_url = "https://gitlab.com/openpowerlifting/opl-data.git"
    
    if is_git_repo(repo_loc) and get_git_repo_name(repo_loc) == 'opl-data':
        try:
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
        subprocess.run(["git", "clone", repo_url, repo_loc], check=True)

    subprocess.run(["tests/check", "--compile"], cwd=repo_loc, check=True)

    shutil.copytree(f"{repo_loc}/build", output_loc, dirs_exist_ok=True)

def is_git_repo(path):
    if not os.path.exists(path):
        return False

    try:
        subprocess.run(["git", "-C", path, "rev-parse", "--is-inside-work-tree"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    
def get_git_repo_name(path):
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
        A function that transforms the OpenPowerlifting bulk CSV 
        into a partitioned parquet file
    """

    # TODO Check if any values are being rounded.

    df = pandas.read_csv(inpath)
    df.to_parquet(outpath)

    return None


