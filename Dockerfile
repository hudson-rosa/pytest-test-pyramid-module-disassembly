# Force amd64 so Chrome + Selenium behave exactly like CI
FROM --platform=linux/amd64 python:3.11-slim-bookworm

# --------------------------------------------------
# Environment
# --------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# --------------------------------------------------
# System dependencies required by Chrome
# --------------------------------------------------
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxss1 \
    libgtk-3-0 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# --------------------------------------------------
# Install Google Chrome (stable)
# --------------------------------------------------
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub \
    | gpg --dearmor -o /usr/share/keyrings/google-linux-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-keyring.gpg] \
       http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Explicit Chrome binary location
ENV CHROME_BIN=/usr/bin/google-chrome
ENV PATH="$PATH:/usr/bin/google-chrome"

# --------------------------------------------------
# App setup
# --------------------------------------------------
WORKDIR /app

# Install Python dependencies first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# --------------------------------------------------
# Default command (can be overridden by CI / act)
# --------------------------------------------------
# # Use official Python base image
# # FROM python:3.11-slim
# FROM --platform=linux/amd64 python:3.11-slim

# # Prevent Python buffering
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     chromium \
#     chromium-driver \
#     wget \
#     curl \
#     unzip \
#     ca-certificates \
#     fonts-liberation \
#     && rm -rf /var/lib/apt/lists/*

# # Set Chrome binary path (important for Selenium)
# ENV CHROME_BIN=/usr/bin/google-chrome

# # Set working directory
# WORKDIR /app

# # Copy dependency file first (for caching)
# COPY requirements.txt .

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy project
# COPY . .

# # Default command (can be overridden)
CMD ["pytest", "tests/unit", "tests/integration", "tests/e2e", "tests/ui/se"]
