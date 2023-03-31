import pandas
import pyarrow.parquet

# This script will ingest data from the OpenPowerlifting repo.

# TODO
    # Choose between getting data from repo or just getting the CSV that they provide
        # getting data from repo will allow for lifter-data as well
    # implementation
        # Just clone the repo and regularly pull to update the contents
            # Once we pull how do we update the transformations


# the downloaded CSV has the revision number at the end

def transform_bulk_csv(inpath, outpath):
    """
        A function that transforms the OpenPowerlifting bulk CSV 
        into a partitioned parquet file
    """

    # TODO Check if any values are being rounded.

    df = pandas.read_csv(inpath)
    df.to_parquet(outpath)

    return None


