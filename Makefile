.PHONY: pre_build

pre_build:
	@pipx --version | grep 1.6.0 ||	@python3 -m pip install --user --upgrade pipx==1.6.0

build: pre_build
	@pipx run build --wheel
	@echo "Building completed!"
