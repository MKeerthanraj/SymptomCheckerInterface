import pickle
from statistics import mode
import numpy as np

data_dict_file = open('pickle_files/data_dict','rb')
data_dict = pickle.load(data_dict_file)
data_dict_file.close()

rf_model_file = open('pickle_files/rf_model','rb')
final_rf_model = pickle.load(rf_model_file)
rf_model_file.close()

nb_model_file = open('pickle_files/nb_model','rb')
final_nb_model = pickle.load(nb_model_file)
nb_model_file.close()

svm_model_file = open('pickle_files/svm_model','rb')
final_svm_model = pickle.load(svm_model_file)
svm_model_file.close()

symptoms_list_file = open('pickle_files/symptoms_list','rb')
symptoms_list = pickle.load(symptoms_list_file)
symptoms_list_file.close()

def predictDisease(symptoms):
    symptoms = symptoms.split(",")
    
    # creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1
        
    # reshaping the input data and converting it
    # into suitable format for model predictions
    input_data = np.array(input_data).reshape(1,-1)
    
    # generating individual outputs
    rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[0]]
    nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(input_data)[0]]
    svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]
    
    # making final prediction by taking mode of all predictions
    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])
    predictions = {
        "rf_model_prediction": rf_prediction,
        "naive_bayes_prediction": nb_prediction,
        "svm_model_prediction": nb_prediction,
        "final_prediction":final_prediction
    }
    return predictions

def getSymptomList():
    return symptoms_list
