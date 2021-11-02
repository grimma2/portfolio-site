
class PromoCodeMixin:
	text = ''
	price = 0

	def setcode(self, text, price):
		self.text = text
		self.price = price


code_models = PromoCodeMixin()
code_first = code_models.setcode('GH47AJE', 800)

