# Birzeit University
## Department of Electrical & Computer Engineering
### First Semester, 2024/2025

# ENCS5343 Computer Vision - Course Project
**Due Date:** January 15, 2025

## 1. Objectives
Use deep learning techniques to solve the problem given in the second assignment.

## 2. Tasks
The assignment contains four main tasks defined as follows:

### Task 1: Build and Train a Custom CNN Network
To build a custom CNN, you need to define the following:

- **Architecture:**
  - **Number of layers:** The depth of the network, typically starting with 1 to 2 convolutional layers and gradually increasing for more complex tasks.
  - **Types of layers:** Convolutional layers, pooling layers (max, average, global), fully connected layers, and potentially other specialized layers (e.g., dropout, batch normalization).
  - **Activation functions:** ReLU (common choice), sigmoid, tanh, or others for specific needs.

- **Convolutional Layer Parameters:**
  - **Number of filters:** Controls the number of feature maps extracted at each layer. More filters can capture more features but increase computational cost.
  - **Filter size:** Determines the receptive field of the filters, often starting with 3x3 or 5x5 and increasing in deeper layers.
  - **Stride:** The step size of the filter movement, affecting the output size and computational complexity.
  - **Padding:** Zero-padding input images to preserve spatial dimensions and capture edge features.

- **Pooling Layer Parameters:**
  - **Pool size:** The size of the pooling window, common choices being 2x2 or 3x3.
  - **Pool type:** Max pooling or average pooling, each with different effects on feature preservation.

- **Fully Connected Layer Parameters:**
  - **Number of neurons:** Related to the complexity of the task and the number of classes for classification.

- **Training Hyperparameters:**
  - **Learning rate:** Controls how much the model's weights are updated during training.
  - **Batch size:** The number of samples processed per training step, affecting gradient updates and convergence speed.
  - **Epochs:** The number of times the model trains on the entire dataset.
  - **Optimizer:** Algorithm for updating model weights (e.g., Adam, SGD, RMSprop).
  - **Regularization:** Techniques to prevent overfitting (e.g., dropout, L1/L2 regularization).

#### Requirements:
1. Design and train various networks with hyperparameter tuning before selecting the simplest network that produces the best results.
2. For each model trained, plot the Loss vs. Epoch number as well as the model's accuracy.

### Task 2: Retrain the Network with Data Augmentation
Data augmentation enhances the diversity and size of your training data without the need for additional data collection. By applying various transformations, models can generalize better to unseen examples and improve overall performance.

- Choose data augmentation techniques relevant to the dataset provided and the task.
- Plot the Loss vs. Epoch number as well as the model's accuracy.
- Compare the results obtained with the results of Task 1.

### Task 3: Train a Well-Known CNN Architecture with Data Augmentation
- Choose a CNN architecture from well-known and published CNN models.
- Train the chosen CNN network with data augmentation.
- Plot the Loss vs. Epoch number as well as the model's accuracy.
- Compare the results obtained with the results of Task 2.

### Task 4: Transfer Learning Using a Pretrained CNN Network
- Use a pretrained CNN network on similar tasks and choose the appropriate transfer learning method to fine-tune the network on the given dataset.
- Plot the Loss vs. Epoch number as well as the model's accuracy.
- Compare the results obtained with the results of Task 3.

## 3. Report
Write a comprehensive report that includes the following sections:

### 1. Introduction

### 2. Experimental Setup and Results
- Describe the evaluation methodology, including the datasets used, evaluation metrics, and experimental setup.
- Present the results of the evaluation, including accuracy and loss curves.
- Analyze the effectiveness of using data augmentation, published CNN networks, and the use of pretrained networks.
- Include results visualization, comparisons, and discussion.

### 3. Conclusion
- Summarize the key findings and achievements of the project.
- Suggest future work and improvements.

---

**End of README**
