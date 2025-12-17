# Optimized Dockerfile for Railway/Render deployment
# Target size: ~1.5 GB (vs 8.6 GB with sentence-transformers)

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (for layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy only necessary application files
COPY api/ ./api/
COPY rag/ ./rag/
COPY vector_store/ ./vector_store/
COPY config.py .
COPY start.py .

# Note: .env is NOT copied - use environment variables from Railway/Render dashboard

# Create non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Start command using Python script (properly handles PORT env var)
CMD ["python", "start.py"]
