import sys
import os
import json
sys.path.append('../../')

from incident_analysis import derive_entropy, dir_path

#open dataset

#Utrecht
utrecht_ordered = ["0","1","4-12","37-703"]
utrecht_shooting = "Q62090804"
with open(f"../output/{utrecht_shooting}/incident_info.json", "r") as infile:
    utrecht_d = json.load(infile)

#mh17
mh17_ordered = ["0-1","2-7","8-15","19-130","318-806",
                "1084-1728"]
mh17 = "Q17374096"
with open(f"../output/{mh17}/incident_info.json", "r") as infile:
    mh17_d = json.load(infile)
#remove MH17 from frames
for condition, tbs in mh17_d.copy().items():
    for tb, value in tbs.items():
        updated_l = list(filter(lambda a: a != "MH17", value["frames"]))
        value["frames"] = updated_l

#curfew riots
dutch_curfew_riots = "Q105077032"
curfew_ordered = ["0-2", "3", "4-7"]
with open(f"../output/{dutch_curfew_riots}/incident_info.json", "r") as infile:
    curfew_d = json.load(infile)

#eurovision
eurovision_song_contest = "Q30973589"
eurovision_ordered = ["-730--620","-604--470","-465--424",
                      "-419--242","-90--28","-26--1","0-13"]
with open(f"../output/{eurovision_song_contest}/incident_info.json", "r") as infile:
    eurovision_d = json.load(infile)
#remove Eurovision from frames
for condition, tbs in eurovision_d.copy().items():
    for tb, value in tbs.items():
        updated_l = list(filter(lambda a: a != "Eurovision", value["frames"]))
        value["frames"] = updated_l

derive_entropy(utrecht_d=utrecht_d,
                    utrecht_ordered=utrecht_ordered,
                    mh17_d=mh17_d,
                    mh17_ordered=mh17_ordered,
                    curfew_d=curfew_d,
                    curfew_ordered=curfew_ordered,
                    eurovision_d=eurovision_d,
                    eurovision_ordered=eurovision_ordered,
                    feature="frames",
                    output_folder=dir_path,
                    verbose=1)

#open dataset

#Utrecht
utrecht_shooting = "Q62090804"
with open(f"../output/{utrecht_shooting}/incident_info_nl.json", "r") as infile:
    utrecht_nl_d = json.load(infile)

#mh17
mh17 = "Q17374096"
with open(f"../output/{mh17}/incident_info_nl.json", "r") as infile:
    mh17_nl_d = json.load(infile)
with open(f"../output/{mh17}/incident_info_en.json", "r") as infile:
    mh17_en_d = json.load(infile)

#curfew riots
dutch_curfew_riots = "Q105077032"
with open(f"../output/{dutch_curfew_riots}/incident_info_nl.json", "r") as infile:
    curfew_nl_d = json.load(infile)

#eurovision
eurovision_song_contest = "Q30973589"
with open(f"../output/{eurovision_song_contest}/incident_info_en.json", "r") as infile:
    eurovision_en_d = json.load(infile)

derive_entropy(utrecht_d=utrecht_nl_d,
                    utrecht_ordered=utrecht_ordered,
                    mh17_d=mh17_nl_d,
                    mh17_ordered=mh17_ordered,
                    curfew_d=curfew_nl_d,
                    curfew_ordered=curfew_ordered,
                    eurovision_d=eurovision_en_d,
                    eurovision_ordered=eurovision_ordered,
                    feature="lexical units",
                    output_folder=dir_path,
                    mh17_en_d=mh17_en_d,
                    verbose=1)
#sys.exit()
