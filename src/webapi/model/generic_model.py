from abc import ABCMeta, abstractmethod, abstractproperty

class GenericModel():
	__metaclass__= ABCMeta

	@abstractmethod
	def train():
		'''train new model'''

	@abstractmethod
	def predict():
		'''predict face label'''

	@abstractmethod
	def update():
		'''update or retrain current model'''

