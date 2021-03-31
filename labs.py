def selectid(ids):
    insertdict = {}
    for idspec in ids:
        try:

            if idspec.tag == "INSDSeq_comment" or idspec.tag == "INSDSeq_create-date"\
                    or idspec.tag == "INSDSeq_definition" or idspec.tag == "INSDSeq_division" or idspec.tag == "INSDSeq_length"\
                    or idspec.tag == "INSDSeq_locus" or idspec.tag == "INSDSeq_moltype" or idspec.tag == "INSDSeq_organism" \
                    or idspec.tag == "INSDSeq_source" or idspec.tag == "INSDSeq_source-db" or idspec.tag == "INSDSeq_topology" \
                    or idspec.tag == "INSDSeq_update-date":
                insertdict[idspec.tag.replace("INSDSeq_", "")] = idspec.text
            elif idspec.tag == "INSDSeq_accession-version":
                insertdict[idspec.tag.replace("INSDSeq_accession-version", "accession_version")] = idspec.text
            elif idspec.tag == "INSDSeq_feature-table":
                features = idspec.findall("./INSDFeature")
                for feature in features:
                    keys = feature.findall("./INSDFeature_key")
                    for key in keys:
                        featurequals = feature.findall("./INSDFeature_quals/")
                        for featurequal in featurequals:
                            featurequalnames = featurequal.findall("./INSDQualifier_name")
                            for featurequalname in featurequalnames:
                                featurequalvalue = featurequal.find("./INSDQualifier_value")
                                if ETree.iselement(featurequalvalue):
                                    insertdict[key.text + "_" + featurequalname.text] = featurequalvalue.text
            elif idspec.tag == "INSDSeq_sequence":
                insertdict[idspec.tag.replace("INSDSeq_", "")] = idspec.text.upper()

            elif idspec.tag == "INSDSeq_references":
                references = idspec.findall("./INSDReference")
                preinsertdict = {}
                x = 1
                for reference in references:
                    refcarrierlistdict = {}

                    # refcarrierlistdict['accession-version'] = insertdict['accession-version'] #maybe won't work
                    refcarrierlistdict['accession_version'] = insertdict['accession_version']
                    reference_id = reference.findall("./INSDReference_reference")
                    reference_authors = reference.findall("./INSDReference_authors")
                    reference_titles = reference.findall("./INSDReference_title")
                    reference_journals = reference.findall("./INSDReference_journal")
                    reference_pubmeds = reference.findall("./INSDReference_pubmed")
                    #print(reference_id)
                    for reference_idx in reference_id:
                        refcarrierlistdict['ref_id'] = reference_idx.text
                        insertdict['ref_id'] = reference_idx.text
                    authorslist = []
                    for reference_au in reference_authors:
                        for reference_aus in reference_au:
                            authorslist.append(reference_aus.text)
                        authorsliststring = "; ".join(authorslist)
                        refcarrierlistdict['ref_au_list'] = authorsliststring
                    for reference_title in reference_titles:
                        refcarrierlistdict['ref_title'] = reference_title.text
                    for reference_journal in reference_journals:
                        refcarrierlistdict['ref_journal'] = reference_journal.text
                    for reference_pubmed in reference_pubmeds:
                        refcarrierlistdict['ref_pubmed'] = reference_pubmed.text
                    insertdict["refcarrierlistdict" + str(x)] = refcarrierlistdict
                    x = x + 1
            else: pass
        except:
            raise ValueError("error in processing")
    return insertdict

import xml.etree.ElementTree as ETree
infile = "./INSD.xml"
outfile = "./outfile.txt"

with open(outfile, "a") as f:
    seqinfilecount = 0
    context = ETree.iterparse(infile, events=("start", "end"))
    for event, elem in context:
        if event == "end" and elem.tag == "INSDSeq":
            ETObj = elem
            if ETree.iselement(ETObj):
                try:
                    insertdict = selectid(ETObj)
                except:
                    raise ValueError("no seq-id")
                insertdict["divid"] = event 
            seqinfilecount += 1
            print(seqinfilecount)
            elem.clear()
print("{} seqs analyzed in 1 file".format(len(insertdict)))