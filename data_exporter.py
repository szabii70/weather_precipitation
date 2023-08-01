import csv

class DataExporter():

	def export_precipitation_datamodel_to_csv(precipitation_data_model):
		'''
		This function requires a PrecipitationDataModel as parameter
		'''
		if type(precipitation_data_model) == PrecipitationDataModel:
			print('ExportToCsv')
		else:
			raise Exception('This function only accepts PrecipitationDataModel as parameter...')