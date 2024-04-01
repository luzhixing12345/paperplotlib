
i = 1

.PHONY: test lexer cover

test:
	@python test/$(i).py

cover:
	coverage run coverage_test.py
	coverage html
