
from constants import BASE_FILE_DIR 
from datetime import datetime
import requests
import logging
import pandas as pd

log = logging.getLogger()


class UrlExtractor:
    file_path_crib = (
        "{category}/{year}-{month: 02d}/{category}-{day: 02d}-{month:02d}-{year}.csv"
)

    def __init__(self, name, url)-> None:
        self.name = name
        self.url = url 
        
        
    def extract(self, date_str: str) -> str:
        
        """Extract data from url, stores it on file_path and return a transformed df
        
        Args:
            date_str (str): run date string with format %Y-%m-%d
            
        Returns:
            str: transformed csv path location
            
    """
        log.info(f"Extracting {self.name}")
        date = datetime.strptime(date_str, "%Y-%m-%d").date() 
        file_path = self.file_path_crib.format(
            category=self.name, year=date. year, month=date.month, day=date.day
        )
        
        m_path = BASE_FILE_DIR/file_path
        m_path.parent.mkdir(parents=True, exist_ok=True)
        
        r = requests.get(self.url) 
        r.encoding="utf-8"
        
        log.info(f"Storing file in {m_path}")
        with open(m_path, "w") as f_out:
            f_out.write(r.text)
            
        return m_path
        
    def transform(self, df: pd.DataFrame) -> pd.DataFrame: 
        
        """Transform raw data and returns it on a pd.Dataframe
        
        Args:
            df (pd.DataFrame): Dataframe to transform
            
        Returns:
            pd.Dataframe: Transformed df
    """  
    
        renamed_cols = {
            'Cod_Loc': 'cod_localidad', 
            'IdProvincia': 'id_provincia',
            'IdDepartamento': 'id_departamento', 
            'direccion': 'domicilio',
            'CP': 'codigo postal',
            'telefono': 'número de teléfono',
            'Mail': 'mail',
            'Web': 'web',
    }
        
        df = df.rename(columns = renamed_cols)

        colum_list = [
            'cod_localidad',
            'id_provincia',
            'id_departamento',
            'categoria',
            'provincia',
            'localidad',
            'nombre',
            'web',
        ]
        
        return df[colum_list] 
    
    
    
class MuseoExtractor(UrlExtractor):
    def transform(self, df: pd.DataFrame)-> pd.DataFrame:
        """Transform raw data and returns it on a pd.Dataframe
        
        Args:
            df (pd.DataFrame): Dataframe to transform
            
        Returns:
            pd.Dataframe: Transformed df
    """  
    
        renamed_cols = {
                'Cod_Loc': 'cod_localidad', 
                'IdProvincia': 'id_provincia',
                'IdDepartamento': 'id_departamento', 
                'direccion': 'domicilio',
                'CP': 'codigo postal',
                'telefono': 'número de teléfono',
                'Mail': 'mail',
                'Web': 'web',
        }
        
        df = df.rename(columns = renamed_cols)

        colum_list = [
        'cod_localidad',
        'id_provincia',
        'id_departamento',
        'categoria',
        'provincia',
        'localidad',
        'nombre',
        'domicilio',
        'codigo postal',
        'número de teléfono',
        'mail',
        'web',
        ]
        
        return df[colum_list]