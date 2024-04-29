import warnings
warnings.filterwarnings('ignore')

from pyhealth.datasets import MIMIC4Dataset

# mimiciv dataset not available in pyhealth?
mimic4_ds = MIMIC4Dataset(
        root="./mimic-iv/hosp/demo",
        tables=["diagnoses_icd", "procedures_icd", "prescriptions","labevents"],
        code_mapping={"NDC": ("ATC", {"target_kwargs": {"level": 3}})},
        refresh_cache=False,
)

# we show the statistics below.
mimic4_ds.stat()