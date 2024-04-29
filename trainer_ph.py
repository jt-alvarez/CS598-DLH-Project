"""
TODO:
    - use Trainer() to initialize a trainer
        - record "jaccard_weighted" and "hamming_loss" during the training
        - use "cpu" as the device,
        - set the experiment name as "drug_recommendation"
        - hint:
        
            Trainer(
                model = ...,
                metrics = ...,
                device = ...,
                exp_name = ...,
            )
            
    - use trainer.train() to start the training
        - set epoch number to 20
        - monitor the "jaccard_weighted" metric, and use "max" as the criterion
        - load the best model when finishing training
        - hint:
            
            Trainer.train(
                train_dataloader = ...,
                val_dataloader = ...,
                epochs = ...,
                monitor = ...,
                monitor_criterion = ...,
            )
"""
from pyhealth.trainer import Trainer

trainer = None

# your code here
trainer = Trainer(
    model = model,
    metrics = ["jaccard_weighted", "hamming_loss"],
    device = "cpu",
    exp_name = "diagnosis_recommendation"
)

trainer.train(
    train_dataloader = train_loader,
    val_dataloader = val_loader,
    epochs = 20,
    monitor = "jaccard_weighted",
    monitor_criterion = "max"
)