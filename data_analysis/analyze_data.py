import os
import random

import pandas as pd


def analyze_img_data():
	'''
	Stats about the image dataset
	'''
	IMG_DIR = './imgs'
	TEST_PATH = os.path.join(IMG_DIR, 'test')
	TRAIN_PATH = os.path.join(IMG_DIR, 'train')
	
	test_num = len([name for name in os.listdir(TEST_PATH) if os.path.isfile(os.path.join(TEST_PATH, name))])

	print "Test data: %d files" % test_num

	for category in os.listdir(TRAIN_PATH):
		category_path = os.path.join(TRAIN_PATH, category)

		if os.path.isdir(category_path):
			category_num = len([name for name in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, name))])
			print "Category %s: %d files" % (category, category_num)

def analyze_content():
	'''
	Stats about the content of the images
	'''
	df = pd.read_csv('imgs/driver_imgs_list.csv')
	columns = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
	subjects = df.drop_duplicates('subject')['subject'].tolist()
	new_df = pd.DataFrame(index=subjects, columns=columns)
	classes = df.drop_duplicates('classname')['classname'].tolist()

	print("Number of drivers: %d" % len(subjects))

	for subject in subjects:
		print("Analyzing subject %s" % subject)
		subject_data = df.loc[df['subject'] == subject]
		row = []
		for class_type in classes:
			images_data = subject_data.loc[df['classname'] == class_type]
			row.append(len(images_data))
		new_df.loc[subject] = row

	print(new_df)
	print(new_df.describe().loc[['mean', 'std', 'min', 'max']])

def get_random_examples():
	df = pd.read_csv('imgs/driver_imgs_list.csv')
	columns = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
	subjects = df.drop_duplicates('subject')['subject'].tolist()
	random_subject = random.choice(subjects)
	random_subject = 'p012'
	print("Analyzing subject %s" % random_subject)
	subject_data = df.loc[df['subject'] == random_subject]

	examples = []
	examples2 = []

	for class_type in columns:
		images_data = subject_data.loc[df['classname'] == class_type]['img'].tolist()
		random_image = random.choice(images_data)
		random_image2 = random.choice(images_data)
		examples.append(class_type + '/' + random_image)
		examples2.append(class_type + '/' + random_image2)

	return examples, examples2
		
if __name__ == '__main__':
	analyze_img_data()
	analyze_content()
	#print(get_random_examples())
