# -*- coding: utf-8 -*-

def home():
	form = FORM(
		DIV(
			LABEL("first number: "),
			INPUT(
				_type = "text",
				_name = "first_number",
				),
			),
		DIV(
			LABEL("second number: "),
			INPUT(
				_type = "text",
				_name = "second_number",
				),
			),
		DIV(
			LABEL("add: "),
			INPUT(
				_type = "radio",
				_name = "selection",
				_value = "add",
				),
			),
		DIV(
			LABEL("multiply: "),
			INPUT(
				_type = "radio",
				_name = "selection",
				_value = "multiply",
				),
			),
		INPUT(
			_type = "submit",
			_value = "Calculate",
			)
		)
	if (form.process().accepted):
		session.first_number = int(form.vars.first_number)
		session.second_number = int(form.vars.second_number)
		if (form.vars.selection == "add"):
			session.operation = "+"
			session.result = session.first_number + session.second_number
		elif (form.vars.selection == "multiply"):
			session.operation = "x"
			session.result = session.first_number * session.second_number
		db.user_entries.insert(
			first_number = session.first_number,
			second_number = session.second_number,
			selected_operation = session.operation,
			user_result = session.result,
			)
		db.commit()
		redirect(
			URL(
				a = "operations_log",
				c = "c01",
				f = "result",
				)
			)
	return dict(
		form = form,
		)
def result():
	home = A(
		"home",
		_href = URL(
			a = "operations_log",
			c = "c01",
			f = "home",
			)
		)
	return dict(
		home = home,
		)
