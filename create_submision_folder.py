import json
import polars as pl
import os

def create_submision_file(team_name: str, task: int, evaluation_context: str, run_id: str, subtask: int, predictions_path: str, 
                          submision_folder: str) -> bool:
    """
    Creates the folder with the predictions according to the guidelines.
    """
    try:
        if exists_submision_folder(team_name):
            predictions = pl.read_csv(predictions_path)
            output = []
            for row in predictions.iter_rows(named=True):
                aux = {}
                aux["test_case"] = "EXIST2025"
                aux["id"] = str(row["id"])
                aux["value"] = row["label"]
                output.append(aux)
            filename = submision_folder + "/" + f"task{task}_{subtask}_{evaluation_context}_{team_name}_{run_id}.json"
            with open(filename, "w") as file:
                json.dump(output, file, indent=4)
            return True
        return False

    except Exception as e:
        print("Ha ocurrido un error:", e)
        return False

def exists_submision_folder(team_name: str) -> bool:
    folder_name = f"exist2025_{team_name}"
    if os.path.exists(folder_name):
        return True
    else:
        try:
            os.mkdir(folder_name)
            return True
        except Exception as e:
            print("Ha ocurrido un error:", e)
            return False
