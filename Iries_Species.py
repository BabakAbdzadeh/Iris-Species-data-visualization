import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = "/home/parallels/MySourceFiles/Data/iris-species/Iris.csv"

def parse(raw_file, delimiter):
	opened_file = open(raw_file)
	csv_data = csv.reader(opened_file, delimiter=delimiter)
	parsed_data = []
	fields = csv_data.next()
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))
	opened_file.close()
	return parsed_data

def visual_location():
	data_file = parse(MY_FILE, ",")
	petal_len = []
 	petal_wid = []
 	sepal_len = []
 	sepal_wid = []
	spicies_list = []

	for dict_item in data_file:
		petal_len.append(dict_item["PetalLengthCm"])
 		petal_wid.append(dict_item["PetalWidthCm"])
 		sepal_len.append(dict_item["SepalLengthCm"])
 		sepal_wid.append(dict_item["SepalWidthCm"])
		spicies_list.append(dict_item["Species"])
	sepal_len = list(map(float, sepal_len))
	sepal_wid = list(map(float, sepal_wid))

	zipped = zip(sepal_len, sepal_wid)
	# zipped.sort()
	color = []
	for spicies in spicies_list:
		if spicies == "Iris-setosa":
			color.append("r")	
		elif spicies == "Iris-versicolor":
			color.append("g")
		elif spicies == "Iris-virginica":
			color.append("b")
	label = "Iris Setosa = RED""\n""Iris Versicolor = GREEN""\n""Iris Virginica = BLUE"
	plt.scatter(sepal_len, sepal_wid,s = 10, c= color,marker = "x", label = label)
	plt.title("SepalWidth vs SepalLength")
	x_label=plt.xlabel("SepalLengthCm")
	x_label.set_color("black")
	y_label=plt.ylabel("SepalWidthCm")
	y_label.set_color("black")
	plt.legend(loc ="upper right", frameon = False)
	plt.show()
#	zipped_petal = zip(petal_len, petal_wid)
#	zipped_sepal = zip(sepal_len, sepal_wid)
#	zipped_xy = zip(list_y, list_x)
#	zipped_xy.sort()
#	plt.scatter(*zip(*zipped_xy))
#	plt.show()





def main():
	visual_location()
if __name__ == "__main__":
	main()
