import time
import pandas as pd

from random import choice
from pathlib import Path

class Helpers:
    def wait(self, initial: int = 1, final: int = 2) -> None:
        """
        Funcion que hace que el programa espere un determinado tiempo
        antes de continuar
        """

        time.sleep(choice([initial, final]))
    
    def saving_path(self, file_name: str = "") -> Path:
        """
        Funcion que retorna el Path en el cual se guardara el archivo con
        los datos obtenidos
        """

        working_dir = Path.cwd()  # Get the current working directory (cwd)
        data_dir = 'result'
        abs_path = Path.joinpath(working_dir, data_dir, f"{file_name}.csv")
        return abs_path
    
    def save_data(self, data: list = [], file_name: str = "") -> None:
        """
        Funcion para guardar los datos obtenidos en un archivo .csv
        """

        df = pd.DataFrame.from_dict(data=data)
        df.set_index("name", inplace=True)
        df.to_csv(self.saving_path(file_name), encoding="utf-8")
