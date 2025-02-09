### Framing Incident Analysis
This package provides functions that extract linguistic information from a corpus of reference texts and perform a frame semantic analysis of the referenced incidents over time. Specifically, the package provides distribution over time of in-text mentions that are linked to structured data, and it provides a distribution of the frames with which the same mentions are annotated.

This package was built and used for the purpose of a thesis Chapter titled "Variation in Framing at Incident Level".

### Prerequisites
Python 3.7.4 was used to create this package. It might work with older versions of Python.

### Resources
A number of GitHub repositories need to be cloned and adapted with novel data. This can be done calling:
```bash
bash install.sh
```

### Python modules
A number of external modules need to be installed, which are listed in **requirements.txt**.
Depending on how you installed Python, you can probably install the requirements using one of following commands:
```bash
pip install -r requirements.txt
```

### Usage
This package comes with different main functions:

# Extract frame semantic information from FramInc corpus
The function framing_an_incident_per_doc() extracts linguistic information from the annotated NAF files (the FramInc corpus) in the DFNDataReleases repository. You can run the function with the following command:

```python
from incident_analysis import framing_an_incident_per_doc, dir_path
from datetime import datetime
import json

with open('../DFNDataReleases/structured/inc2lang2doc2subevents.json', "r") as infile:
    subevents_dict = json.load(infile)

utrecht_shooting = "Q62090804"
utrecht_shooting_date = datetime(2019,3,18)

framing_an_incident_per_doc(project="test_release",
                            incident=utrecht_shooting,
                            language="nl",
                            event_date=utrecht_shooting_date,
                            subevents_dict=subevents_dict,
                            output_folder=dir_path,
                            start_from_scratch=False,
                            verbose=1)
```
The following parameters are specified:
* **project** the label of the research project
* **incident** the wikidata identifier of the incident
* **language** the language in which the reference texts are overwritten
* **event_date** the date on which the incident occurred.
* **subevents_dict** a dictionary that links a selection of mentions in FramInc to the incident ID, as a means of post-annotation curation.
* **output_folder** the path to the current package. The helper functions will use this path to create new folders to which extracted data will be exported.
* **start_from_scratch**: if True, remove all existing output
* **verbose**: 1: descriptive stats 2: more stats 3: lots of stats

After running the example, you observe an **output** folder in this directory. Its nested structure is as follows:

output
  WIKIDATA_ID
    corpus
      LANGUAGE
        *.json

Run the python script test_framing_per_doc.py in the **test** folder to extract and export the information from all four incidents in FramInc in English and Dutch to the output folder.

# Plot timeline
The function plot_timeline() takes the json files from a specified incident and exports a plot of publication dates. You can run the function with the following command:

```python
from incident_analysis import plot_timeline, dir_path

utrecht_shooting = "Q62090804"

plot_timeline(incident=utrecht_shooting,
                output_folder=dir_path,
                start_from_scratch=False,
                verbose=1)
```
The following parameters are specified:
* **incident** the wikidata identifier of the incident
* **output_folder** the path to the current package. The helper functions will use this path to create new folders to which extracted data will be exported.
* **start_from_scratch**: if True, remove all existing output
* **verbose**: 1: print path to which the plot is exported.

After running the example, you will find a timeline.PDF in the WIKIDATA_ID subfolder of **output**.

Run the python script test_plot_timeline.py in the **test** folder to plot the timelines of all four incidents in FramInc.

# incident information to json
The function incident_info() extracts information from the previously created jsons and groups that information under temporal distance classes. You can run the function with the following command:

```python
from incident_analysis import incident_analysis, dir_path

utrecht_shooting = "Q62090804"
time_buckets_utrecht = {"0":range(0,1),
                        "1":range(1,2),
                        "4-12":range(4,13),
                        "37-703":range(37,704)}

incident_info(incident=utrecht_shooting,
                  time_buckets=time_buckets_utrecht,
                  output_folder=f"{dir_path}/output/{utrecht_shooting}",
                  verbose=3)
```
The following parameters are specified:
* **incident** the wikidata identifier of the incident
* **time_buckets** dictionary of temporal distance classes
* **output_folder** the path to the current package. The helper functions will use this path to create new folders to which the new json file will be exported.
* **verbose**: >=1: print path to json file; >=2: print descriptive statistics

After running the example, you will find the new json folder in the WIKIDATA_ID subfolder of **output**. Run the python script test_info_analysis.py in the **test** folder to produce the json folders of all four incidents in FramInc.

# Frames Analysis
The function frame_lu_analysis() runs an analysis of the frames an plots their head distribution across temporal distance classes. You can run the function with the following command:

```python
from incident_analysis import frame_lu_analysis, dir_path
import json

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
```
The following parameters are specified:
* **incident** the wikidata identifier of the incident
* **data_dict** dictionary of frame semantic information grouped under temporal distance classes
* **condition** whether the frames are linked to the anchor incident or climax incidents
* **ordered_time_buckets** a list with the temporal distance classes in fixed order
* **output_folder** the path to the current package. The helper functions will use this path to create new folders to which the plots will be exported
* **dimension** the linguistic dimension along which the analysis is conducted
* **types_tokens** print a table with a frequency distribution of frames in terms of types and tokens
* **verbose**: >=1: print path to pdf or tex file; >=2: print descriptive statistics

After running the example, you observe a **figures** folder (containing line plots) and a **tables** (containing frequency distributions) in the respective WIKIDATA_ID subfolder of **output**. Its nested structure is as follows:

output
  WIKIDATA_TD
    figures
      frames
        *.pdf
    tables
      frames
        *.tex

Run the python script test_frames_analysis.py in the **test** folder to produce frame plots for all four incidents in FramInc.

#Lexical unit analysis
The function frame_lu_analysis() also runs an analysis of the lexical units and plots their head distribution across temporal distance classes. You can run the function with the following command:

```python
from incident_analysis import frame_lu_analysis, dir_path
import json

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
                verbose=1)
```
The following parameters are specified:
* **incident** the wikidata identifier of the incident
* **data_dict** dictionary of frame semantic information grouped under temporal distance classes
* **condition** whether the frames are linked to the anchor incident or climax incidents
* **ordered_time_buckets** a list with the temporal distance classes in fixed order
* **output_folder** the path to the current package. The helper functions will use this path to create new folders to which the plots will be exported
* **dimension** the linguistic dimension along which the analysis is conducted
* **language** the language of the dataset
* **verbose**: >=1: print path to pdf file; >=2: print descriptive statistics

After running the example, plots are exported to the **lexical units** subfolder of **figures**. Run the python script test_lexical_unit_analysis.py in the **test** folder to produce lexical unit plots for all four incidents in FramInc.

#construction analysis
The function construction_analysis() runs an analysis of constructions and plots their relative distribution across temporal distance classes. You can run the function with the following command:

```python
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
```
The following parameters are specified:
* **incident** the wikidata identifier of the incident
* **data_d** dictionary of frame semantic information grouped under temporal distance classes
* **ordered_l** a list with the temporal distance classes in fixed order
* **output_folder** the path to the current package. The helper functions will use this path to create new folders to which the plots will be exported
* **n_columns** the number of temporal distance classes
* **verbose**: >=1: print path to pdf file

After running the example, plots are exported to the **constructions** subfolder of **figures**. Run the python script test_construction_analysis.py in the **test** folder to produce construction plots for all four incidents in FramInc.

### Authors
* **Levi Remijnse** (levi_remijnse@hotmail.com)

### License
This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
