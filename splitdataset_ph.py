import numpy as np
from pyhealth.datasets.splitter import split_by_patient
from pyhealth.datasets import split_by_patient, get_dataloader
from pyhealth.tasks import condition_recommendation_mimic4_fn

dataset = mimic4_ds.set_task(task_fn=condition_recommendation_mimic4_fn)

# print 1st sample:
first_sample = dataset.samples[0]
print(first_sample)

np.random.seed(1234)

# data split
train_dataset, val_dataset, test_dataset = split_by_patient(dataset, [0.8, 0.1, 0.1])

# create dataloaders (they are <torch.data.DataLoader> object)
train_loader = get_dataloader(train_dataset, batch_size=64, shuffle=True)
val_loader = get_dataloader(val_dataset, batch_size=64, shuffle=False)
test_loader = get_dataloader(test_dataset, batch_size=64, shuffle=False)

