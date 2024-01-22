import click
from extractors import MuseoExtractor, UrlExtractor 
import pandas as pd
from constants import BASE_FILE_DIR
from cfg import (
    museo_ds,
    cines_ds,
    espacios_ds,)

from loaders import (
    CineInsightsLoader,
    SizeByCategoryLoader,
    SizeBySourceLoader,
    SizeByCatProvLoader,
)

import logging

log = logging.getLogger()

extractors_dict = {
    "museo": MuseoExtractor (museo_ds ["name"], museo_ds ["url"]), 
    "cines": UrlExtractor (cines_ds ["name"], cines_ds ["url"]),
    "espacios": UrlExtractor (espacios_ds ["name"], espacios_ds["url"]),
}


def extract_raws (date_str: str) -> list[str]: 
    
    """Run extractors
Args:
        date_str (str): run date with format yyyy-mm-dd
        
Returns:
        list[str]: list of stored data file paths
    """
    

    file_paths = dict()
    for name, extractor in extractors_dict.items(): 
        file_path = extractor.extract(date_str) 
        file_paths[name] = file_path
    
    return file_paths

def merge_raw(file_paths: list [str], out_file_path: str) -> str: 
    """merge raw data and stores it on out_file_path
        Args:
            file_paths (list [str]): list of raw data location out_file_path (str): destination location
        Returns:
            str: destination location
    """
    dfs_transformed = list()
    for name, extractor in extractors_dict.items(): 
        pd.read_csv(file_paths [name]) 
        df = dft
        extractor.transform(df)
        dfs_transformed.append(dft)
    pd.concat(dfs_transformed, axis=0).to_csv(out_file_path)
    return out_file_path

@click.command()
@click.option("--date", help="run date in format yyyy-mm-dd")

def run_pipeline (date: str) -> None: 

    """Run the pipeline
Args:
    date (str): Job date format YYYY-MM-DD
""" 

    # Extract
    log.info("Extracting")

    file_paths = extract_raws(date)
    
    # Transform
    merge_path = BASE_FILE_DIR / "merge_df_{date}.csv" 
    merge_raw(file_paths, merge_path)
    
    # Load
    log.info("Loading")
    CineInsightsLoader().load_table(file_paths["cines"]) 
    SizeByCategoryLoader().load_table(merge_path)
    SizeBySourceLoader().load_table(file_paths) 
    SizeByCatProvLoader().load_table(merge_path)
    log.info("Done")
    

if __name__ == "__main__":
    run_pipeline()

