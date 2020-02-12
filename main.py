import csv
import sys
import xlrd
import constant as CONSTANT

image_size = CONSTANT.IMAGE_SIZE
data = csv.DictReader(open("data/dataset.csv"))
data_labels, data_images = [], []

# Prints the provided sample in ASCII art
def print_number(sample):
    for x in range(image_size):
        string_frag = ''
        for y in range(image_size):
            string_frag = (string_frag + '1') if sample[(x * 28) + y] != 0 else (string_frag + '0')
        print(string_frag)
    print("\n") 

# Returns the distance (i.e. the number of differing pixels) between a test sample and a training sample
def distance(test_sample, train_sample):
    total_distance = 0
    for index in range(image_size**2):
        total_distance = (total_distance + 1) if test_sample[index] != train_sample[index] else (total_distance)
    return total_distance 

# Reads in each row from the dataset which contains a label and 28*28 pixels containing 0 or 1.
for row in data:
    data_labels.append(int(row["label"]))
    image = []
    for index in range(0, image_size**2):
        image.append(int(row['pixel' + str(index)]))
    data_images.append(image)

# Seperates the dataset into a training set and a testing set
train_labels = data_labels[0:CONSTANT.TRAIN_SET_SIZE]
train_images = data_images[0:CONSTANT.TRAIN_SET_SIZE]
test_labels = data_labels[CONSTANT.TRAIN_SET_SIZE + 1 : CONSTANT.TRAIN_SET_SIZE + CONSTANT.TEST_SET_SIZE]
test_images = data_images[CONSTANT.TRAIN_SET_SIZE + 1 : CONSTANT.TRAIN_SET_SIZE + CONSTANT.TEST_SET_SIZE]

# Begins classification of testing data
counter, num_correct = 0, 0
for img in test_images:
    min_dist = []
    for x in range(0, len(train_images)):
        min_dist.append((str(train_labels[x]), distance(img, train_images[x])))

    # Sorts lists of distances in ascending order
    k_list = (sorted(min_dist, key=lambda tup: tup[1]))[0:CONSTANT.K]
    num_occurrences = [0] * 10

    # Generates # of classifications for each possible digit where the digit matches its index in the list
    for choice in k_list:
        index = int(choice[0])
        value = num_occurrences[index] + 1
        num_occurrences[index] = value   

    common_label = (max(num_occurrences))
    classification = num_occurrences.index(common_label)
    num_correct = (num_correct + 1) if classification == test_labels[counter] else (num_correct)
    counter += 1

print("Classifications Summary: \n-------------------------")
print("Correct: " + str(num_correct) + "\nIncorrect: " + str(len(test_images) - num_correct))
print("Accuracy: " + str(((num_correct / (num_correct + (len(test_images) - num_correct))) * 100)))