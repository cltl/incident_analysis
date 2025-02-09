import sys
import os
import json
sys.path.append('../../')

from incident_analysis import frame_lu_analysis, dir_path

###Eurovision Song Contest 2021###

eurovision_song_contest = "Q30973589"
eurovision_ordered = ["-730--620","-604--470","-465--424",
                      "-419--242","-90--28","-26--1","0-13"]
with open(f"../output/{eurovision_song_contest}/incident_info.json", "r") as infile:
    eurovision_d = json.load(infile)

for condition, tbs in eurovision_d.copy().items(): #remove Eurovision from frames
    for tb, value in tbs.items():
        updated_l = list(filter(lambda a: a != "Eurovision", value["frames"]))
        value["frames"] = updated_l

frame_lu_analysis(incident=eurovision_song_contest,
                data_dict=eurovision_d,
                condition="anchor",
                ordered_time_buckets=eurovision_ordered,
                output_folder=dir_path,
                dimension="frames",
                figsize=(8,4),
                types_tokens=True,
                verbose=1)

frame_lu_analysis(incident=eurovision_song_contest,
                data_dict=eurovision_d,
                condition="non-anchor",
                ordered_time_buckets=eurovision_ordered,
                output_folder=dir_path,
                dimension="frames",
                figsize=(8,4),
                bbox_to_anchor=(1, 1),
                verbose=1)

###Dutch curfew riots###

riots_ordered = ["0-2", "3", "4-7"]
dutch_curfew_riots = "Q105077032"

with open(f"../output/{dutch_curfew_riots}/incident_info.json", "r") as infile:
    riots_d = json.load(infile)

frame_lu_analysis(incident=dutch_curfew_riots,
                data_dict=riots_d,
                condition="anchor",
                ordered_time_buckets=riots_ordered,
                output_folder=dir_path,
                dimension="frames",
                types_tokens=True,
                verbose=1)

frame_lu_analysis(incident=dutch_curfew_riots,
                data_dict=riots_d,
                condition="non-anchor",
                ordered_time_buckets=riots_ordered,
                output_folder=dir_path,
                dimension="frames",
                bbox_to_anchor=(1, 1),
                verbose=1)

###MH17###

mh17_ordered = ["0-1","2-7","8-15","19-130","318-806","1084-1728"]
mh17 = "Q17374096"

with open(f"../output/{mh17}/incident_info.json", "r") as infile:
    mh17_d = json.load(infile)

for condition, tbs in mh17_d.copy().items(): #remove MH17 from frames
    for tb, value in tbs.items():
        updated_l = list(filter(lambda a: a != "MH17", value["frames"]))
        value["frames"] = updated_l

frame_lu_analysis(incident=mh17,
                data_dict=mh17_d,
                condition="anchor",
                ordered_time_buckets=mh17_ordered,
                output_folder=dir_path,
                dimension="frames",
                types_tokens=True,
                verbose=1)

frame_lu_analysis(incident=mh17,
                data_dict=mh17_d,
                condition="non-anchor",
                ordered_time_buckets=mh17_ordered,
                output_folder=dir_path,
                dimension="frames",
                bbox_to_anchor=(1, 1),
                verbose=1)

###Utrecht shooting###
utrecht_ordered = ["0","1","4-12","37-703"]
utrecht_shooting = "Q62090804"

with open(f"{dir_path}/output/{utrecht_shooting}/incident_info.json", "r") as infile:
    utrecht_d = json.load(infile)

frame_lu_analysis(incident=utrecht_shooting,
                data_dict=utrecht_d,
                condition="anchor",
                ordered_time_buckets=utrecht_ordered,
                output_folder=dir_path,
                dimension="frames",
                types_tokens=True,
                verbose=1)

frame_lu_analysis(incident=utrecht_shooting,
                data_dict=utrecht_d,
                condition="non-anchor",
                ordered_time_buckets=utrecht_ordered,
                output_folder=dir_path,
                dimension="frames",
                bbox_to_anchor=(1, 1),
                verbose=1)

sys.exit()
