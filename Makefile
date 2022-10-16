.PHONY: dev
dev:
	@echo "Starting development server..."
	@uvicorn main:app --reload
