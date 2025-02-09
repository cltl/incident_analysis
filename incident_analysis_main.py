from .path_utils import get_naf_paths
from .historical_distance_utils import prepare_timeline_plot, get_titles_and_publication_dates, timestamps_collection, validate_publication_date, calculate_difference
from .xml_utils import check_attendee_fe, deps, check_if_annotated, get_raw_text, get_title, get_frames, get_frame_elements, get_lemmas, get_entity_links, get_sentence_info, get_compound_info, get_determiner_info, doc_variation, move_fes, remove_deprecated_mws, descriptive_stats, add_unexpressed_coresets
from .output_utils import create_output_folder, variation_to_excel
from .incident_info_utils import extract_compounds, compile_terms, info_incident, extract_info
from .validation_utils import map_subevents_to_instance
from .frames_analysis_utils import plot_lu_offset, lu_distribution, remove_named_events, frames_distribution, plot_figure, restructure_data, type_selection, reorder_time_buckets
from .entropy_utils import calculate_entropy, entropy_to_latex
from .construction_utils import extract_construction_info, barplot
from lxml import etree
import json
import glob
import os
import pickle
import pandas as pd
import numpy as np
import pprint
from collections import defaultdict
from matplotlib import pyplot as plt
import random

def derive_entropy(utrecht_d,
                    utrecht_ordered,
                    mh17_d,
                    mh17_ordered,
                    curfew_d,
                    curfew_ordered,
                    eurovision_d,
                    eurovision_ordered,
                    feature,
                    output_folder,
                    mh17_en_d=None,
                    verbose=0):
    """calculates the entropy values for all incidents between time buckets"""
    if feature == "frames":
        frames_entropy_d = {}
        utrecht_ent_d = calculate_entropy(utrecht_d, feature, utrecht_ordered)
        frames_entropy_d["Utrecht shooting"] = utrecht_ent_d
        mh17_ent_d = calculate_entropy(mh17_d, feature, mh17_ordered)
        frames_entropy_d["Malaysia Airlines flight 17"] = mh17_ent_d
        curfew_ent_d = calculate_entropy(curfew_d, feature, curfew_ordered)
        frames_entropy_d["Dutch curfew riots"] = curfew_ent_d
        eurovision_ent_d = calculate_entropy(eurovision_d, feature, eurovision_ordered)
        frames_entropy_d["Eurovsion Song Contest 2021"] = eurovision_ent_d
        entropy_to_latex(frames_entropy_d, feature, output_folder, verbose)
    if feature == "lexical units":
        frames_entropy_d = {}
        utrecht_ent_d = calculate_entropy(utrecht_d, feature, utrecht_ordered)
        frames_entropy_d["Utrecht shooting (nl)"] = utrecht_ent_d
        mh17_ent_d = calculate_entropy(mh17_d, feature, mh17_ordered)
        frames_entropy_d["Malaysia Airlines flight 17 (nl)"] = mh17_ent_d
        mh17_ent_en_d = calculate_entropy(mh17_en_d, feature, mh17_ordered)
        frames_entropy_d["Malaysia Airlines flight 17 (en)"] = mh17_ent_en_d
        curfew_ent_d = calculate_entropy(curfew_d, feature, curfew_ordered)
        frames_entropy_d["Dutch curfew riots (nl)"] = curfew_ent_d
        eurovision_ent_d = calculate_entropy(eurovision_d, feature, eurovision_ordered)
        frames_entropy_d["Eurovsion Song Contest 2021 (en)"] = eurovision_ent_d
        entropy_to_latex(frames_entropy_d, feature, output_folder, verbose)
    return

###variation in framing incidents analysis###

def construction_analysis(incident,
                            data_d,
                            ordered_l,
                            output_folder,
                            n_columns,
                            figsize=None,
                            start_from_scratch=False,
                            verbose=0):
    """conduct analysis of variation in constructions in reference to an incident"""
    create_output_folder(output_folder=f"{output_folder}/output/{incident}/figures/constructions",
                        start_from_scratch=start_from_scratch,
                        verbose=verbose)
    unordered_tbs, plot_data = extract_construction_info(incident_d=data_d,
                                                            ordered_tbs=ordered_l)
    barplot(plot_data=plot_data,
            n_columns=n_columns,
            ordered_l=ordered_l,
            output_folder=output_folder,
            incident=incident,
            textspan="fulltext",
            fs=figsize,
            verbose=verbose)
    unordered_tbs, plot_data = extract_construction_info(incident_d=data_d,
                                                            ordered_tbs=ordered_l,
                                                            textspan=range(2,5))
    barplot(plot_data=plot_data,
            n_columns=n_columns,
            ordered_l=ordered_l,
            output_folder=output_folder,
            incident=incident,
            textspan="firstlines",
            fs=figsize,
            verbose=verbose)
    unordered_tbs, plot_data = extract_construction_info(incident_d=data_d,
                                                            ordered_tbs=ordered_l,
                                                            textspan=range(1,2))
    barplot(plot_data=plot_data,
            n_columns=n_columns,
            ordered_l=ordered_l,
            output_folder=output_folder,
            incident=incident,
            textspan="headline",
            fs=figsize,
            verbose=verbose)

    return

def frame_lu_analysis(incident,
                    data_dict,
                    condition,
                    ordered_time_buckets,
                    output_folder,
                    dimension,
                    figsize=None,
                    bbox_to_anchor=None,
                    start_from_scratch=False,
                    types_tokens=False,
                    language=None,
                    verbose=0):
    """conduct analysis of variation in frames or lexical units in reference to an incident"""
    create_output_folder(output_folder=f"{output_folder}/output/{incident}/figures/{dimension}",
                        start_from_scratch=start_from_scratch,
                        verbose=verbose)
    create_output_folder(output_folder=f"{output_folder}/output/{incident}/tables/{dimension}",
                        start_from_scratch=start_from_scratch,
                        verbose=verbose)
    plot_data = restructure_data(incident_d=data_dict,
                                condition=condition,
                                ordered_l=ordered_time_buckets,
                                dimension=dimension,
                                output_folder=output_folder,
                                incident=incident,
                                language=language,
                                verbose=verbose)
    plot_figure(plot_data=plot_data,
                output_folder=output_folder,
                condition=condition,
                incident=incident,
                verbose=verbose,
                specified_bbox_to_anchor=bbox_to_anchor,
                specified_figsize=figsize,
                dimension=dimension,
                language=language)

    if types_tokens == True:
        distribution(incident_d=data_dict,
                        output_folder=output_folder,
                        incident=incident,
                        verbose=verbose,
                        ordered_l=ordered_time_buckets)

    if dimension == "lexical units" and condition == "anchor":
        if incident == "Q17374096" or incident == "Q30973589":
            remove_named_events(data_d=data_dict)
        d = lu_distribution(incident_d=data_dict)
        plot_lu_offset(x=d["TDC"],
                        y=d["avg ratio"],
                        ordered_l=ordered_time_buckets,
                        output_folder=output_folder,
                        incident=incident,
                        dimension=dimension,
                        condition=condition,
                        language=language,
                        specified_figsize=figsize,
                        verbose=verbose)
    return


###temporal distance plotting###

def plot_timeline(incident,
                    titles_to_ignore=None,
                    output_folder=None,
                    start_from_scratch=True,
                    language=None,
                    verbose=0):
    """extract the publication dates from an incident subcorpus and plot a timeline"""
    data_space_d = get_titles_and_publication_dates(incident=incident,
                                                    output_folder=output_folder,
                                                    titles_to_ignore=titles_to_ignore)
    hdd_l, publication_l = prepare_timeline_plot(data_space_d)

    ax1 = plt.figure(dpi=300)
    plt.plot(hdd_l, publication_l)
    plt.xlabel('N days')
    plt.ylabel('N reference texts')

    if output_folder != None:
        create_output_folder(output_folder=f"{output_folder}/output/{incident}",
                            start_from_scratch=start_from_scratch,
                            verbose=verbose)

    pdf_path = f"{output_folder}/output/{incident}/timeline.pdf"
    plt.savefig(pdf_path)
    if verbose:
        print(f"exported timeline to {pdf_path}")

###incident analysis###

def incident_info(incident,
                        time_buckets,
                        output_folder,
                        threshold=None,
                        language=None,
                        long_short=False,
                        verbose=0):
    """perform incident analysis for a given corpus, incident and time buckets"""
    all_incident_info_d = {}
    conditions = ["all", "anchor", "non-anchor"]

    for condition in conditions:
        incident_info = info_incident(condition, time_buckets, incident, output_folder, language)
        all_incident_info_d[condition] = incident_info

    if verbose >= 2:
        extract_info(all_incident_info_d)

    if language == None:
        if long_short == False:
            json_path = f"{output_folder}/incident_info.json"
        else:
            json_path = f"{output_folder}/incident_info_long-short.json"
    else:
        if long_short == False:
            json_path = f"{output_folder}/incident_info_{language}.json"
        else:
            json_path = f"{output_folder}/incident_info_long-short_{language}.json"

    with open(json_path, 'w') as outfile:
        json.dump(all_incident_info_d, outfile, indent=4, sort_keys=True)

    if verbose:
        print(f"exported incident info to {json_path}")
    return

###preprocessing###

def framing_an_incident_per_doc(project,
                                incident,
                                language,
                                event_date,
                                subevents_dict=None,
                                output_folder=None,
                                start_from_scratch=True,
                                verbose=0):
    """create a dictionary with all relevant info about the framing of a specified incident per document"""
    naf_paths = get_naf_paths(project=project,
                                incident=incident,
                                language=language,
                                verbose=verbose)
    timestamps = timestamps_collection(naf_paths[incident])
    known_timestamps, unknown_timestamps = validate_publication_date(event_date=event_date,
                                                                    timestamps=timestamps,
                                                                    verbose=verbose)
    historical_distance_list = calculate_difference(list_of_timestamps=known_timestamps,
                                                    event_date=event_date)

    titles = []
    n_entity_links = 0
    n_lus = 0
    n_fes = 0
    n_tokens = 0

    if output_folder != None:
        create_output_folder(output_folder=f"{output_folder}/output/{incident}/corpus/{language}",
                            start_from_scratch=start_from_scratch,
                            verbose=verbose)

    for path in naf_paths[incident]:
        doc_tree = etree.parse(path)
        root = doc_tree.getroot()

        if check_if_annotated(root, language) == False:
            if verbose >= 2:
                print()
                print(f"{path} has no srl layer")
                print()
            continue

        raw_text = get_raw_text(root)
        title = get_title(root)
        if verbose >= 2:
            print(title)
        titles.append(title)
        frames_dict = get_frames(root)
        frame_elements_dict = get_frame_elements(root)
        lemmas_dict = get_lemmas(root)
        remove_deprecated_mws(frames_dict, lemmas_dict, frame_elements_dict)
        entity_links_dict = get_entity_links(root, verbose)
        sentence_dict = get_sentence_info(root)
        compound_dict = get_compound_info(root, lemmas_dict, language)
        move_fes(frame_elements_dict, compound_dict)
        determiner_dict = get_determiner_info(root)
        deps_dict = deps(root)
        add_unexpressed_coresets(frames_dict, frame_elements_dict, verbose)
        check_attendee_fe(frames_dict, frame_elements_dict, verbose)

        doc_variation_dict = doc_variation(title=title,
                                            entity_links_dict=entity_links_dict,
                                            frames_dict=frames_dict,
                                            fe_dict=frame_elements_dict,
                                            lemma_dict=lemmas_dict,
                                            sentence_dict=sentence_dict,
                                            det_dict=determiner_dict,
                                            compound_dict=compound_dict,
                                            deps_dict=deps_dict,
                                            hdd_list=historical_distance_list,
                                            raw_text=raw_text,
                                            root=root)

        if subevents_dict != None:
            map_subevents_to_instance(incident=incident,
                                        language=language,
                                        subevents_dict=subevents_dict,
                                        doc_variation_dict=doc_variation_dict,
                                        verbose=verbose)

        json_path = f"{output_folder}/output/{incident}/corpus/{language}/{title}.json"
        with open(json_path, 'w') as outfile:
            json.dump(doc_variation_dict, outfile, indent=4, sort_keys=True)

        if verbose >= 2:
            print(f"exported variation dict to {json_path}")

        entity_links, lus, fes = descriptive_stats(language=language,
                                                    title=title,
                                                    incident=incident,
                                                    entity_links_dict=entity_links_dict,
                                                    frames_dict=frames_dict,
                                                    fe_dict=frame_elements_dict,
                                                    subevents_dict=subevents_dict)
        n_entity_links += len(entity_links)
        n_lus += len(lus)
        n_fes += len(fes)
        n_tokens += len(lemmas_dict)

    if verbose:
        print()
        print("descriptive statistics")
        print("number of reference texts:", len(titles))
        print("average number of tokens:", round(n_tokens/len(titles)))
        print("number of entity links:", n_entity_links)
        print("number of lexical units:", n_lus)
        print("number of core frame elements", n_fes)
    return

def extract_hdd(project,
                incident_dict,
                output_folder=None,
                start_from_scratch=True,
                verbose=0):
    """extract historical distance in days from naf files and provide a range of data points per incident"""
    data_space_dict = {}

    for incident, info in incident_dict.items():
        for language in info["languages"]:
            data_space = []
            naf_paths = get_naf_paths(project=project,
                                        incident=incident,
                                        language=language,
                                        verbose=verbose)
            timestamps = timestamps_collection(naf_paths[incident])
            known_timestamps, unknown_timestamps = validate_publication_date(event_date=info["date"],
                                                                            timestamps=timestamps,
                                                                            verbose=verbose)
            historical_distance_list = calculate_difference(list_of_timestamps=known_timestamps,
                                                            event_date=info["date"])
            for doc in historical_distance_list:
                historical_distance = doc['historical distance']
                data_space.append(historical_distance)
            sorted_data_space = sorted(data_space)
            data_space_dict[incident][language] = sorted_data_space
    print(data_space_dict)
    return
