import csv
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

MY_FILE = "/home/parallels/Mytest/Data/iris-species/Iris.csv"

def parse(raw_file, delimiter):
	opened_file = open(raw_file)
	csv_data = csv.reader(opened_file, delimiter=delimiter)
	parsed_data = []
	fields = csv_data.next()
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))
	opened_file.close()
	return parsed_data
def petalLen_id():
	data_file = parse(MY_FILE, ",")
	setosa_petal_len = []
	setosa_id = []

	versicolor_petal_len = []
	versicolor_id = []

	virginica_petal_len = []
	virginica_id = []

	setosa = []
	versicolor = []
	virginica = []
	iris_setosa = mlines.Line2D([], [], color = 'red', marker = '_', linestyle = 'none', markersize = 			10, label = "Iris-setosa" )
	iris_versicolor = mlines.Line2D([], [], color = 'green', marker = '_', linestyle = 'none', 			markersize = 10, label = "Iris-versicolor" )
	iris_virginica = mlines.Line2D([], [], color = 'blue', marker = '_', linestyle = 'none', 			markersize = 10, label = "Iris-virginic" )

	for item in data_file:
		if item["Species"] == 'Iris-setosa':
			setosa_petal_len.append(float(item["PetalLengthCm"]))
			setosa_id.append(int(item["Id"]))
			setosa.append(item["Species"])
		
		if item["Species"] == 'Iris-versicolor':
			versicolor_petal_len.append(float(item["PetalLengthCm"]))
			versicolor_id.append(int(item["Id"]))
			versicolor.append(item["Species"])
		
		if item["Species"] == 'Iris-virginica':
			virginica_petal_len.append(float(item["PetalLengthCm"]))
			virginica_id.append(int(item["Id"]))
			virginica.append(item["Species"])
	# petal_len = list(map(float, petal_len))
	# id_list = list(map(int, id_list))

	plt.plot(setosa_id,setosa_petal_len, color = "red" , label = "Iris-setosa")
	plt.plot(versicolor_id,versicolor_petal_len, color = "green")
	plt.plot(virginica_id, virginica_petal_len, color = "blue")
	x_label=plt.xlabel("Id")
	x_label.set_color("black")
	y_label=plt.ylabel("PetalLengthCm")
	y_label.set_color("black")
	plt.legend(handles=[iris_setosa, iris_versicolor, iris_virginica])
	plt.savefig('PetalLenght_vs_PetalId.png')
	
	plt.show()


def main():
	petalLen_id()
if __name__ == "__main__":
	main()
