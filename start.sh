set -e

uvicorn app.main:app \
    --host=0.0.0.0 \
    --port=8080 \
    --reload \
    --log-level=debug \
    --use-colors
