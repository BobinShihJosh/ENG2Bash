# ENG2Bash

### Demo(Hugging Face): https://huggingface.co/Josh98/t5-large-t5large-English-to-BASH

## Model Specs
# T5-Large English to BASH

This repository contains a fine-tuned version of the T5-Large model for English-to-Bash translation. The model was trained on the None dataset and achieved the following results on the evaluation set:

- **Loss:** 0.6448
- **Nl2bash M:** 0.7181
- **Gen Len:** 14.2079

## Training Procedure

### Training Hyperparameters

The following hyperparameters were used during training:

- Learning Rate: 4e-05
- Train Batch Size: 16
- Eval Batch Size: 16
- Seed: 42
- Optimizer: Adam with betas=(0.9, 0.999) and epsilon=1e-08
- LR Scheduler Type: Linear
- Number of Epochs: 10

### Training Results

| Training Loss | Epoch | Step  | Validation Loss | Nl2bash M | Gen Len  |
|---------------|-------|-------|------------------|-----------|----------|
| 1.8995        | 1.0   | 561   | 1.1364           | 0.5124    | 13.7261  |
| 1.1669        | 2.0   | 1122  | 0.9093           | 0.5966    | 13.9349  |
| 0.9508        | 3.0   | 1683  | 0.8024           | 0.645     | 13.7716  |
| 0.8426        | 4.0   | 2244  | 0.7366           | 0.6696    | 13.9492  |
| 0.7574        | 5.0   | 2805  | 0.6994           | 0.6888    | 14.099   |
| 0.6884        | 6.0   | 3366  | 0.6756           | 0.6946    | 14.2498  |
| 0.6301        | 7.0   | 3927  | 0.6573           | 0.7101    | 14.3782  |
| 0.6031        | 8.0   | 4488  | 0.6476           | 0.7165    | 14.1793  |
| 0.5536        | 9.0   | 5049  | 0.6465           | 0.7164    | 14.1989  |
| 0.5443        | 10.0  | 5610  | 0.6448           | 0.7181    | 14.2079  |

## How to Use

[Include instructions on how to use the model, any dependencies, and examples.]

## License

[Specify the license under which your model and code are distributed.]

## Acknowledgments

[Give credit to any external sources, libraries, or datasets that you used or modified.]
