# veggie-vision
Vegetable Classification

This script trains a custom image classification model using TensorFlow and Keras, leveraging a pre-trained EfficientNetV2B0 base model for efficiency. It utilizes data from a local directory, incorporates data augmentation for increased robustness, and employs callbacks for early stopping and model checkpointing. The model is trained with a specified learning rate and evaluated on the test dataset using categorical crossentropy and accuracy metrics. A confusion matrix is created to measure classification performance. Finally, it includes a custom predict function to evaluate a single image.
