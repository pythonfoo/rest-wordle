.PHONY: dev
dev:
	@echo "Starting development server..."
	@uvicorn rest_wordle:app --reload
