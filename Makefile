
i = 1

# 判断平台是 Windows 还是 Linux
ifeq ($(OS),Windows_NT)
RM = del
else
RM = rm
endif

.PHONY: test lexer cover

test:
	@python test/$(i).py

cover:
	coverage run coverage_test.py
	coverage html

all:
	@python all.py $(i)

clean:
	$(RM) *.png