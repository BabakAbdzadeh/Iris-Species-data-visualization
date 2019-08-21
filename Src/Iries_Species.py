import csv
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

MY_FILE = "csv file address here !!"

def parse(raw_file, delimiter):
	opened_file = open(raw_file)
	csv_data = csv.reader(opened_file, delimiter=delimiter)
	parsed_data = []
	fields = csv_data.next()
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))
	opened_file.close()
	return parsed_data

def visual_len_wid():
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

	
	
	color = []
	
	for spicies in spicies_list:
		if spicies == "Iris-setosa":
			color.append("r")	
		elif spicies == "Iris-versicolor":
			color.append("g")
		elif spicies == "Iris-virginica":
			color.append("b")
	iris_setosa = mlines.Line2D([], [], color = 'red', marker = 's', linestyle = 'none', markersize = 10, label = "Iris-setosa" )
	iris_versicolor = mlines.Line2D([], [], color = 'green', marker = 's', linestyle = 'none', markersize = 10, label = "Iris-versicolor" )
	iris_virginica = mlines.Line2D([], [], color = 'blue', marker = 's', linestyle = 'none', markersize = 10, label = "Iris-virginic" )


 
	#label = "Iris Setosa = RED""\n""Iris Versicolor = GREEN""\n""Iris Virginica = BLUE"
	plt.scatter(sepal_len, sepal_wid,s = 10, c= color,marker = "s")
	plt.title("SepalWidth vs SepalLength")
	x_label=plt.xlabel("SepalLengthCm")
	x_label.set_color("black")
	y_label=plt.ylabel("SepalWidthCm")
	y_label.set_color("black")
	plt.legend(handles=[iris_setosa, iris_versicolor, iris_virginica])
	plt.show()
	plt.savefig("LenghtVsWidth.png")








def main():
	visual_len_wid()
if __name__ == "__main__":
	main()
