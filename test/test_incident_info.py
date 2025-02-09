import sys
import os
sys.path.append('../../')

from incident_analysis import incident_info, dir_path

time_buckets_mh17 = {"0-1": range(0,2),
                    "2-7": range(2,8),
                    "8-15": range(8,16),
                    "19-130": range(19,131),
                    "318-806": range(318,807),
                    "1084-1728": range(1084,1729)}
mh17 = "Q17374096"

curfew = "Q105077032"

time_buckets_curfew = {"0-2": range(0,3),
                    "3": range(3,4),
                    "4-7": range(4,8)}

utrecht = "Q62090804"

time_buckets_utrecht = {"0":range(0,1),
                        "1":range(1,2),
                        "4-12":range(4,13),
                        "37-703":range(37,704)}

song_contest = "Q30973589"

time_buckets_contest = {"-730--620": range(-730,-619),
                        "-604--470": range(-604,-469),
                        "-465--424": range(-465,-423),
                        "-419--242": range(-419,-241),
                        "-90--28": range(-90,-27),
                        "-26--1": range(-26,0),
                        "0-13": range(0,14)}

#time buckets, langage-specific
incident_info(incident=mh17,
                    time_buckets=time_buckets_mh17,
                    output_folder=f"{dir_path}/output/Q17374096",
                    language="en",
                    verbose=3)

incident_info(incident=mh17,
                    time_buckets=time_buckets_mh17,
                    output_folder=f"{dir_path}/output/Q17374096",
                    language="nl",
                    verbose=3)

incident_info(incident=curfew,
                    time_buckets=time_buckets_curfew,
                    output_folder=f"{dir_path}/output/Q105077032",
                    language="nl",
                    verbose=3)

incident_info(incident=utrecht,
                    time_buckets=time_buckets_utrecht,
                    output_folder=f"{dir_path}/output/Q62090804",
                    language="nl",
                    verbose=3)

incident_info(incident=song_contest,
                    time_buckets=time_buckets_contest,
                    output_folder=f"{dir_path}/output/{song_contest}",
                    language="en",
                    verbose=3)

#time buckets, underspecific

incident_info(incident=mh17,
                    time_buckets=time_buckets_mh17,
                    output_folder=f"{dir_path}/output/Q17374096",
                    verbose=3)

incident_info(incident=curfew,
                    time_buckets=time_buckets_curfew,
                    output_folder=f"{dir_path}/output/Q105077032",
                    verbose=3)

incident_info(incident=utrecht,
                    time_buckets=time_buckets_utrecht,
                    output_folder=f"{dir_path}/output/Q62090804",
                    verbose=3)

incident_info(incident=song_contest,
                    time_buckets=time_buckets_contest,
                    output_folder=f"{dir_path}/output/{song_contest}",
                    verbose=3)

#sys.exit()
