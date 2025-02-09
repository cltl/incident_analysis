import sys
import os
import json
sys.path.append('../../')

from incident_analysis import frame_lu_analysis, dir_path

#Utrecht
utrecht_ordered = ["0","1","4-12","37-703"]
utrecht_shooting = "Q62090804"
with open(f"../output/{utrecht_shooting}/incident_info_nl.json", "r") as infile:
    utrecht_nl_d = json.load(infile)

frame_lu_analysis(incident=utrecht_shooting,
                data_dict=utrecht_nl_d,
                condition="anchor",
                ordered_time_buckets=utrecht_ordered,
                output_folder=dir_path,
                dimension="lexical units",
                language="nl",
                verbose=2)

frame_lu_analysis(incident=utrecht_shooting,
                data_dict=utrecht_nl_d,
                condition="non-anchor",
                ordered_time_buckets=utrecht_ordered,
                output_folder=dir_path,
                dimension="lexical units",
                bbox_to_anchor=(1, 1),
                language="nl",
                verbose=2)

#sys.exit()

#mh17
mh17_ordered = ["0-1","2-7","8-15","19-130","318-806","1084-1728"]
mh17 = "Q17374096"
with open(f"../output/{mh17}/incident_info_nl.json", "r") as infile:
    mh17_nl_d = json.load(infile)

frame_lu_analysis(incident=mh17,
                data_dict=mh17_nl_d,
                condition="anchor",
                ordered_time_buckets=mh17_ordered,
                output_folder=dir_path,
                dimension="lexical units",
                bbox_to_anchor=(1, 1),
                language="nl",
                verbose=2)

frame_lu_analysis(incident=mh17,
                data_dict=mh17_nl_d,
                condition="non-anchor",
                ordered_time_buckets=mh17_ordered,
                output_folder=dir_path,
                dimension="lexical units",
                bbox_to_anchor=(1, 1),
                language="nl",
                verbose=2)

with open(f"../output/{mh17}/incident_info_en.json", "r") as infile:
    mh17_en_d = json.load(infile)

frame_lu_analysis(incident=mh17,
                data_dict=mh17_en_d,
                condition="anchor",
                ordered_time_buckets=mh17_ordered,
                output_folder=dir_path,
                dimension="lexical units",
                language="en",
                verbose=2)

frame_lu_analysis(incident=mh17,
                data_dict=mh17_en_d,
                condition="non-anchor",
                ordered_time_buckets=mh17_ordered,
                output_folder=dir_path,
                dimension="lexical units",
                bbox_to_anchor=(1, 1),
                language="en",
                verbose=2)

#curfew riots
riots_ordered = ["0-2", "3", "4-7"]
dutch_curfew_riots = "Q105077032"
with open(f"../output/{dutch_curfew_riots}/incident_info_nl.json", "r") as infile:
    riots_nl_d = json.load(infile)

frame_lu_analysis(incident=dutch_curfew_riots,
                data_dict=riots_nl_d,
                condition="anchor",
                ordered_time_buckets=riots_ordered,
                output_folder=dir_path,
                dimension="lexical units",
                bbox_to_anchor=(1, 1),
                language="nl",
                verbose=2)

frame_lu_analysis(incident=dutch_curfew_riots,
                data_dict=riots_nl_d,
                condition="non-anchor",
                ordered_time_buckets=riots_ordered,
                output_folder=dir_path,
                dimension="lexical units",
                bbox_to_anchor=(1, 1),
                language="nl",
                verbose=2)

#eurovision
eurovision_song_contest = "Q30973589"
eurovision_ordered = ["-730--620","-604--470","-465--424","-419--242","-90--28","-26--1","0-13"]
with open(f"../output/{eurovision_song_contest}/incident_info_en.json", "r") as infile:
    eurovision_en_d = json.load(infile)

frame_lu_analysis(incident=eurovision_song_contest,
                data_dict=eurovision_en_d,
                condition="anchor",
                ordered_time_buckets=eurovision_ordered,
                output_folder=dir_path,
                dimension="lexical units",
                figsize=(8,4),
                language="en",
                verbose=2)

frame_lu_analysis(incident=eurovision_song_contest,
                data_dict=eurovision_en_d,
                condition="non-anchor",
                ordered_time_buckets=eurovision_ordered,
                output_folder=dir_path,
                dimension="lexical units",
                figsize=(8,4),
                bbox_to_anchor=(1, 1),
                language="en",
                verbose=2)
