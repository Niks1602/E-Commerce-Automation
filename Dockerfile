#FROM mcr.microsoft.com/playwright/python:v1.50.0-noble
#
#WORKDIR /app
#
## Install required build tools (skip if evdev not needed)
#RUN apt-get update && apt-get install -y \
#    build-essential \
#    python3-dev \
#    libevdev-dev \
#    && rm -rf /var/lib/apt/lists/*
#
#COPY requirements.txt .
#
## FIX for PEP 668 issue
#RUN pip install --break-system-packages --no-cache-dir -r requirements.txt
#
## 🧠 THIS installs the browsers
#RUN python -m playwright install --with-deps
#
#COPY . .
#
#ENTRYPOINT ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure-results"]
FROM mcr.microsoft.com/playwright/python:v1.50.0-noble

WORKDIR /app

# Install required build tools (skip if evdev not needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libevdev-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies
COPY requirements.txt .

# FIX for PEP 668 issue
RUN pip install --break-system-packages --no-cache-dir -r requirements.txt

# 🧠 Install Playwright browsers and dependencies
RUN python -m playwright install --with-deps

# Copy all project files
COPY . .

# 📝 Ensure allure-results directory exists
RUN mkdir -p /app/allure-results

# Clean up allure-results folder every time the container starts
ENTRYPOINT ["/bin/bash", "-c", "rm -rf /app/allure-results/* && behave -f allure_behave.formatter:AllureFormatter -o /app/allure-results"]

