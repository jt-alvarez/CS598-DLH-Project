def condition_recommendation_mimic4_fn(patient):
    samples = []
    for visit in patient:

        # step 1: obtain visit-level information, conditions, procedures, and drugs
        conditions = visit.get_code_list(table="diagnoses_icd")
        procedures = visit.get_code_list(table="procedures_icd")
        drugs = visit.get_code_list(table="prescriptions")
        labs = visit.get_code_list(table="labevents")


        # step 2: exclusion criteria: cohort selection
        if len(conditions) * len(procedures) * len(drugs) * len(labs) == 0: continue

        # step 3: assemble the sample
        # REMEMBER: the key here will be the "feature_keys" and "label_key" for initializing the downstream model
        samples.append(
            {
                "visit_id": visit.visit_id,
                "patient_id": patient.patient_id,
                "conditions": conditions,
                "procedures": procedures,
                "drugs": drugs,
                "labs": labs,
                "label": conditions,
            }
        )

    # step 4: patient-level cohort selection and other process
    # exclude patients with less than 2 visit
    if len(samples) < 2:
        return []

    """ 
    Add historical visit (use "conditions" key as an example)
        before this step:
            samples[0]["conditions"]: 1st visit
            samples[1]["conditions"]: 2nd visit
            samples[2]["conditions"]: 3rd visit
            ...
        
        after this step:
            samples[0]["conditions"]: [1st visit]
            samples[1]["conditions"]: [1st visit, 2nd visit]
            samples[2]["conditions"]: [1st visit, 2nd visit, 3rd visit]
            ...
    """
    samples[0]["conditions"] = [samples[0]["conditions"]]
    samples[0]["procedures"] = [samples[0]["procedures"]]
    samples[0]["drugs"] = [samples[0]["drugs"]]
    samples[0]["labs"] = [samples[0]["labs"]]

    for i in range(1, len(samples)):
        samples[i]["conditions"] = samples[i - 1]["conditions"] + [
            samples[i]["conditions"]
        ]
        samples[i]["procedures"] = samples[i - 1]["procedures"] + [
            samples[i]["procedures"]
        ]
        samples[i]["drugs"] = samples[i - 1]["drugs"] + [
            samples[i]["drugs"]
        ]
        samples[i]["labs"] = samples[i-1]["labs"] + [
            samples[i]["labs"]
        ]
    for i in range(len(samples)):
        samples[i]["conditions"][i] = []

    return samples