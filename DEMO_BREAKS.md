# DEMO BREAKS — FOR FILMING ONLY
# =====================================
# These files show what FAILURES look like in the pipeline.
# Use these to demonstrate why each workflow step matters.
#
# DO NOT commit these to main — create a separate branch for each demo!
# e.g: git checkout -b demo/broken-secret

# 
# BREAK 1: Secret Scan failure
# 
# Add this to any .py file, then push.
# TruffleHog will detect the AWS key pattern and FAIL the pipeline.
#
# FAKE_AWS_KEY = "AKIAIOSFODNN7EXAMPLE"
# FAKE_API_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
#
# Camera note: Show the Actions tab → red X on secret-scan job
# Zoom in on the TruffleHog output showing exactly which file + line number


# 
# BREAK 2: Test failure
# 
# In app/app.py, change:
# return jsonify({"message": "Hello from FRESHKIDS!", ...})
# to:
# return jsonify({"message": "Hello World!", ...})
#
# The test expects "Hello from FRESHKIDS!" so pytest will FAIL.
#
# Camera note: Show the test output — pytest lists exactly which assertion failed
# Good teaching moment: the pipeline stops HERE, Docker never even runs


# 
# BREAK 3: Docker build failure 
# 
# In Dockerfile, change:
# FROM python:3.12-slim
# to:
# FROM python:3.99-slim (this version doesn't exist)
#
# Camera note: Show Docker build step failing with "manifest unknown"
# Good for explaining: even if tests pass, a broken Docker config stops deployment


# 
# FILMING ORDER SUGGESTION
# 
# 1. Show the happy path first — all 4 stages going green 
# 2. Then break secret scan — show pipeline stops immediately 
# 3. Fix it, then break tests — show pipeline stops at stage 2 
# 4. Fix it, show successful Docker push to Docker Hub
# 5. Show staging auto-deploy, then trigger production with approval gate
