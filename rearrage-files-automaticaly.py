import os
import shutil
import pandas as pd

participants_dataframe = pd.read_table(filepath_or_buffer='tsv-files/participants.tsv')

def return_df_by_disorder(dataframe,value):
    return dataframe.loc[dataframe['diag'] == value, :].reset_index(drop=True)

def get_participants_series(dataframe,value):
    df = return_df_by_disorder(dataframe,value)
    return df.loc[:,'participant_id']

participants_autism = get_participants_series(participants_dataframe,1).to_list()
participants_bipolar = get_participants_series(participants_dataframe,7).to_list()
participants_schizophrenia= get_participants_series(participants_dataframe,4).to_list()
participants_mdd = get_participants_series(participants_dataframe,2).to_list()

dir_from = '/media/elements/Datasets/SRPBS_OPEN/data/'

dir_to = '/media/elements/Datasets/SRPBS_OPEN/'

directory = {'Autism_SBPNS':participants_autism, 'Bipolar_SBPNS':participants_bipolar, 'Schizophrenia_SBPNS':participants_schizophrenia, 'MDD_SBPNS':participants_mdd}

#Copiar resultados de los escáneres a la nueva ruta
for main_folder,subfolders in directory.items():
    new_dir_to = os.path.join(dir_to,main_folder)
    if not os.path.exists(new_dir_to):
        os.makedirs(new_dir_to)
    for subfolder in subfolders:
        full_prev = os.path.join(dir_from,subfolder)
        try:
            shutil.copytree(full_prev,os.path.join(new_dir_to,subfolder))
            print(f"Directorios copiados! {os.listdir(os.path.join(new_dir_to,subfolder))}")
        except Exception as error:
            print(f"Se ha generado el error: {error}")        



