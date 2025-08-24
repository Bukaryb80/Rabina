# Unzip Rabina.zip
Expand-Archive -Path "Rabina.zip" -DestinationPath "Rabina" -Force

# Navigate into the Rabina folder
Set-Location -Path "Rabina"

# Initialize Git
git init

# Clone the Rabina repository
gh repo clone bukaryb80/Rabina .

# Add remote origin (redundant if clone succeeded, but included for completeness)
git remote add origin https://github.com/bukaryb80/Rabina.git

# Stage all files
git add .

# Commit with message
git commit -m "Initial launch files for Haddy"

# Push to main branch
git push origin main
