"""
TODO: 
    - initialize a Transformer model by pyhealth.models.Transformer
    - use "conditions", "procedures", and "drugs_all" as the features
    - use "drugs" as the predicted targets
    - refer to https://colab.research.google.com/drive/1LcXZlu7ZUuqepf269X3FhXuhHeRvaJX5?usp=sharing
    
Hint:
    Transformer(
        dataset = ...,
        feature_keys = ...,
        label_key = ...,
        mode = ...,
    )
"""

from pyhealth.models import Transformer

model = None
# I have doubt on feature_keys on which features we can pass to model
model = Transformer(
    dataset = dataset,
    feature_keys =["conditions_all",
                  "procedures",
                  "drugs",
                  "labs",
                  ],
    label_key = "conditions",
    mode = "multilabel"
)