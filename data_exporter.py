import csv
from precipitation_data_model import PrecipitationDataModel

class DataExporter():

    def export_precipitation_datamodel_to_csv(self, precipitation_data_model, csv_file):
        '''
        export_precipitation_datamodel_to_csv(PrecipitationDataModel, str)

        This function exports the attributes of the PrecipitationDataModel as a csv row into the "csv_file".csv file.
        '''
        if type(precipitation_data_model) == PrecipitationDataModel and type(csv_file) == str:

            try:
                with open(csv_file, mode='r', newline='') as file:
                    obj = csv.reader(file)
            except:
                with open(csv_file, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['City name','Date time', 'First quarter', 'Second quarter', 'Third quarter', 'Fourth quarter'])

            data = (
                precipitation_data_model.city_name.title(),
                precipitation_data_model.date_time.strftime("%m/%d/%Y, %H:%M:%S"),
                precipitation_data_model.precipitation_data[0],
                precipitation_data_model.precipitation_data[1],
                precipitation_data_model.precipitation_data[2],
                precipitation_data_model.precipitation_data[3],
            )
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
        else:
            raise Exception('Thic function only accepts: PrecipitationDataModel, str!')