result = trainer.evaluate(test_loader)
#raise NotImplementedError

print (result)

# obtain the true label, predicted probability, evaluation loss 
y_true, y_prob, loss = trainer.inference(test_loader)

from pyhealth.metrics import multilabel_metrics_fn


result = multilabel_metrics_fn(y_true, y_prob, metrics=["pr_auc_samples", "f1_weighted", "recall_macro", "precision_micro"])
#raise NotImplementedError

print (result)