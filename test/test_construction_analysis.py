import sys
import os
import json
sys.path.append('../../')

from incident_analysis import construction_analysis, dir_path

#Utrecht
utrecht_ordered = ["0","1","4-12","37-703"]
utrecht_shooting = "Q62090804"
with open(f"../output/{utrecht_shooting}/incident_info.json", "r") as infile:
    utrecht_d = json.load(infile)

construction_analysis(incident=utrecht_shooting,
                        data_d=utrecht_d,
                        ordered_l=utrecht_ordered,
                        output_folder=dir_path,
                        n_columns=4,
                        verbose=1)

#sys.exit()

#mh17
mh17_ordered = ["0-1","2-7","8-15","19-130","318-806","1084-1728"]
mh17 = "Q17374096"
with open(f"../output/{mh17}/incident_info.json", "r") as infile:
    mh17_d = json.load(infile)

construction_analysis(incident=mh17,
                        data_d=mh17_d,
                        ordered_l=mh17_ordered,
                        output_folder=dir_path,
                        n_columns=6,
                        verbose=1)

#curfew riots
riots_ordered = ["0-2", "3", "4-7"]
dutch_curfew_riots = "Q105077032"
with open(f"../output/{dutch_curfew_riots}/incident_info.json", "r") as infile:
    riots_d = json.load(infile)

construction_analysis(incident=dutch_curfew_riots,
                        data_d=riots_d,
                        ordered_l=riots_ordered,
                        output_folder=dir_path,
                        n_columns=3,
                        verbose=1)

#eurovision
eurovision_song_contest = "Q30973589"
eurovision_ordered = ["-730--620","-604--470","-465--424","-419--242","-90--28","-26--1","0-13"]
with open(f"../output/{eurovision_song_contest}/incident_info_en.json", "r") as infile:
    eurovision_d = json.load(infile)

construction_analysis(incident=eurovision_song_contest,
                        data_d=eurovision_d,
                        ordered_l=eurovision_ordered,
                        output_folder=dir_path,
                        n_columns=7,
                        figsize=(8,4),
                        verbose=1)
