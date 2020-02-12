# K-Nearest Neighbours
## Algorith Overview
This implementation of the K-Nearest Neighbours algorithm can be broken down into the following steps:
1. Load the dataset containing the handwritten digits
2. Partition the dataset into a training set and a testing set
3. For each image in the testing set:
    1. Calculate the distance between the test image and all training images.
    2. Sort the calculated distances in ascending order and keep the K smallest distances.
    3. Get the most frequent label from the K smallest distances.
    4. Return the prediction.

## Dataset
The dataset [Digit Recognizer](https://www.kaggle.com/c/digit-recognizer/overview) contains 40,000 samples of 28x28 images each of which represent a handwritten numerical digit. Note: the dataset used is the *"train.csv"* which was partitioned into a training subset and a testing subset.

## Results
In order to evaluate this implementation of K-Nearest Neighbours an experiment was run using 35,000 training samples, 250 test samples and a K value of 7. This implementation was able to correctly classify the handwritten digit 81.53% of the time.

## Execution
Download the dataset and copy it into the *data/* directory. Rename the file to *"dataset.csv"* then from the command line run:
`python main.py`

## Reference Materials
1. [A Quick Introduction to K-Nearest Neighbors Algorithm](https://blog.usejournal.com/a-quick-introduction-to-k-nearest-neighbors-algorithm-62214cea29c7)
2. [Introduction to k-Nearest Neighbors: A powerful Machine Learning Algorithm](https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/)
3. [Handwritten Character Recognition using K-NN Classification Algorithm](https://pdfs.semanticscholar.org/bd25/04d5432319e605e05c5f67ba39ae6041f897.pdf)
