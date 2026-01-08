#!/bin/bash
# Production build script for frontend

# Build the React application
npm run build

# Optimize the build
echo "Optimizing build..."
# Add any additional optimization steps here

echo "Production build complete!"
echo "Files are located in the 'build' directory"