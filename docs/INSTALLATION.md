# Installation Guide

Complete installation and setup instructions for the Manhattan Power Grid AI-Powered Smart Grid Operations Center.

---

## Table of Contents

- [System Requirements](#system-requirements)
- [Step 1: Install Python](#step-1-install-python)
- [Step 2: Install SUMO](#step-2-install-sumo)
- [Step 3: Clone Repository](#step-3-clone-repository)
- [Step 4: Setup Virtual Environment](#step-4-setup-virtual-environment)
- [Step 5: Install Dependencies](#step-5-install-dependencies)
- [Step 6: Configure Environment Variables](#step-6-configure-environment-variables)
- [Step 7: Verify Installation](#step-7-verify-installation)
- [Troubleshooting](#troubleshooting)

---

## System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, macOS 10.14+, Ubuntu 18.04+
- **CPU**: Intel i5 or AMD equivalent (4 cores)
- **RAM**: 8GB
- **GPU**: Integrated graphics (Intel HD 4000+)
- **Storage**: 2GB free space
- **Browser**: Chrome 90+, Edge 90+, Firefox 88+

### Recommended Requirements
- **OS**: Windows 11, macOS 12+, Ubuntu 22.04+
- **CPU**: Intel i7/i9 or AMD Ryzen 7/9 (8+ cores)
- **RAM**: 16GB or more
- **GPU**: Dedicated GPU (NVIDIA GTX 1060+, AMD RX 580+)
- **Storage**: 5GB free space (SSD recommended)
- **Monitor**: 1920x1080 or higher, 144Hz for best performance
- **Browser**: Latest Chrome or Edge (best WebGL performance)

---

## Step 1: Install Python

### Windows

1. Download Python 3.8 or later from [python.org](https://www.python.org/downloads/)
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Run the installer with default settings
4. Verify installation:
   ```cmd
   python --version
   ```
   Expected output: `Python 3.8.x` or higher

### macOS

```bash
# Using Homebrew (recommended)
brew install python@3.10

# Verify installation
python3 --version
```

### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Verify installation
python3 --version
```

---

## Step 2: Install SUMO

### Windows

1. **Download SUMO**
   - Visit [Eclipse SUMO Downloads](https://eclipse.org/sumo/)
   - Download the latest Windows installer (1.15.0 or newer)
   - Run the installer (default installation path recommended)

2. **Set Environment Variable**
   - Right-click "This PC" → Properties → Advanced System Settings
   - Click "Environment Variables"
   - Under "System Variables", click "New"
   - Variable name: `SUMO_HOME`
   - Variable value: `C:\Program Files (x86)\Eclipse\Sumo`
   - Click OK on all dialogs

3. **Verify Installation**
   ```cmd
   echo %SUMO_HOME%
   sumo --version
   ```

### macOS

```bash
# Using Homebrew
brew tap dlr-ts/sumo
brew install sumo

# Set SUMO_HOME in ~/.zshrc or ~/.bash_profile
echo 'export SUMO_HOME="/opt/homebrew/opt/sumo/share/sumo"' >> ~/.zshrc
source ~/.zshrc

# Verify
echo $SUMO_HOME
sumo --version
```

### Linux (Ubuntu/Debian)

```bash
# Add SUMO repository
sudo add-apt-repository ppa:sumo/stable
sudo apt update

# Install SUMO
sudo apt install sumo sumo-tools sumo-doc

# Set SUMO_HOME in ~/.bashrc
echo 'export SUMO_HOME="/usr/share/sumo"' >> ~/.bashrc
source ~/.bashrc

# Verify
echo $SUMO_HOME
sumo --version
```

---

## Step 3: Clone Repository

```bash
# Clone the repository
git clone https://github.com/XGraph-Team/SumoXPypsa.git

# Navigate to project directory
cd SumoXPypsa
```

---

## Step 4: Setup Virtual Environment

### Windows

```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# You should see (venv) in your command prompt
```

### macOS/Linux

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# You should see (venv) in your terminal prompt
```

---

## Step 5: Install Dependencies

```bash
# Ensure virtual environment is activated (you should see (venv) in prompt)

# Upgrade pip
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt

# This will install:
# - Flask (web framework)
# - PyPSA (power grid simulation)
# - NumPy, Pandas (data processing)
# - scikit-learn (machine learning)
# - tensorflow/keras (deep learning)
# - traci (SUMO Python API)
# - openai (chatbot AI)
# - and other dependencies
```

**Expected installation time**: 3-10 minutes depending on internet speed

---

## Step 6: Configure Environment Variables

### Option 1: Create .env File (Recommended)

Create a file named `.env` in the project root directory:

```env
# OpenAI Configuration (required for chatbot)
OPENAI_API_KEY=sk-your-openai-api-key-here

# Mapbox Configuration (required for map)
MAPBOX_TOKEN=pk.your-mapbox-token-here

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_PORT=5000

# SUMO Configuration
SUMO_GUI=False  # Set to True to show SUMO GUI

# Performance Settings
MAX_VEHICLES=1000
TARGET_FPS=144
```

### Option 2: System Environment Variables

**Windows**:
```cmd
set OPENAI_API_KEY=sk-your-openai-api-key-here
set MAPBOX_TOKEN=pk.your-mapbox-token-here
```

**macOS/Linux**:
```bash
export OPENAI_API_KEY=sk-your-openai-api-key-here
export MAPBOX_TOKEN=pk.your-mapbox-token-here
```

### Getting API Keys

#### OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key (starts with `sk-`)
6. **Note**: Requires billing setup, costs ~$0.01-0.05 per session

#### Mapbox Token
1. Go to [Mapbox Account](https://account.mapbox.com/)
2. Sign up or log in
3. Navigate to Access Tokens
4. Copy your default public token (starts with `pk.`)
5. **Note**: Free tier includes 50,000 map loads/month

---

## Step 7: Verify Installation

### Quick Verification

```bash
# Ensure virtual environment is activated
# Ensure you're in the project directory

# Run the application
python main_complete_integration.py
```

**Expected output**:
```
[INFO] Starting Manhattan Power Grid System...
[INFO] Initializing SUMO Manager...
[INFO] Initializing Power System...
[INFO] Initializing V2G Manager...
[INFO] Initializing ML Engine...
[INFO] Initializing Ultra-Intelligent Chatbot...
[SUCCESS] All systems initialized!
 * Running on http://127.0.0.1:5000
```

### Test in Browser

1. Open your browser (Chrome or Edge recommended)
2. Navigate to: `http://localhost:5000`
3. You should see:
   - Manhattan map loading
   - Chatbot window opening
   - Control panel on the left
   - Performance stats top-left

4. **Test basic functionality**:
   - Type `start vehicles` in chatbot
   - Press Enter
   - Vehicles should appear on the map
   - Chatbot should respond: "✅ Starting vehicle simulation..."

### Run Test Suite (Optional)

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run basic tests
pytest tests/ -v

# Expected: All tests passing
```

---

## Troubleshooting

### Issue: "Python not found"

**Solution**:
- Windows: Reinstall Python with "Add to PATH" checked
- macOS/Linux: Use `python3` instead of `python`

### Issue: "SUMO_HOME not set"

**Solution**:
```bash
# Windows
set SUMO_HOME=C:\Program Files (x86)\Eclipse\Sumo

# macOS/Linux
export SUMO_HOME=/usr/share/sumo  # or your SUMO installation path
```

### Issue: "Module not found" errors

**Solution**:
```bash
# Ensure virtual environment is activated
# You should see (venv) in your prompt

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Issue: "OpenAI API error"

**Solution**:
- Verify your API key is correct in `.env`
- Check your OpenAI account has billing enabled
- Verify internet connection
- Test with: `curl https://api.openai.com/v1/models -H "Authorization: Bearer YOUR_KEY"`

### Issue: "Map not loading"

**Solution**:
- Verify Mapbox token in `.env`
- Check browser console for errors (F12)
- Try different browser (Chrome recommended)
- Disable browser extensions (ad blockers)

### Issue: "Low FPS / Poor Performance"

**Solution**:
- Enable hardware acceleration in browser settings
  - Chrome: `chrome://settings/` → Advanced → System → Use hardware acceleration
- Close other browser tabs
- Reduce vehicle count: `start 50 vehicles` instead of 500
- Update graphics drivers
- Use recommended GPU settings

### Issue: "Port 5000 already in use"

**Solution**:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <process_id> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9

# Or change port in main_complete_integration.py
```

### Issue: "Database locked" error

**Solution**:
```bash
# Delete the database file
rm manhattan_grid.db  # It will be recreated

# Or on Windows
del manhattan_grid.db
```

### Issue: "TraCI connection failed"

**Solution**:
- Ensure SUMO is properly installed
- Verify SUMO_HOME environment variable
- Check no other SUMO instance is running
- Try setting `SUMO_GUI=True` in .env to see SUMO errors

---

## Platform-Specific Notes

### Windows

- Use PowerShell or Command Prompt (admin recommended)
- Disable Windows Defender real-time scanning for project folder (optional, improves performance)
- If using WSL2, install Linux version instead

### macOS

- If using Apple Silicon (M1/M2), some dependencies may need Rosetta 2
- Grant terminal permissions if prompted
- Use latest macOS for best Metal (GPU) support

### Linux

- Ubuntu 22.04 LTS recommended for best compatibility
- May need to install additional packages: `sudo apt install build-essential`
- Wayland users: Switch to X11 for better WebGL performance

---

## Performance Optimization

### Browser Settings

**Chrome/Edge** (Recommended):
1. Navigate to `chrome://flags/`
2. Enable:
   - `#enable-webgl2-compute-context`
   - `#enable-gpu-rasterization`
   - `#enable-zero-copy`
3. Restart browser

**Firefox**:
1. Navigate to `about:config`
2. Set `webgl.force-enabled` to `true`
3. Set `layers.acceleration.force-enabled` to `true`

### System Settings

**Windows**:
- Graphics Settings → Add Python → High Performance
- Power Plan → High Performance

**macOS**:
- Energy Saver → Disable "Automatic graphics switching"

**Linux**:
- Install proprietary NVIDIA drivers if using NVIDIA GPU
- For AMD: Install latest Mesa drivers

---

## Next Steps

After successful installation:

1. **Read the User Guide**: [README.md](../README.md#-user-guide)
2. **Explore Features**: [FEATURES.md](FEATURES.md)
3. **Learn Chatbot Commands**: [CHATBOT_COMMANDS.md](CHATBOT_COMMANDS.md)
4. **Try Demo Scenarios**:
   - `run v2g scenario`
   - `blackout scenario`
5. **Check API Reference**: [API_REFERENCE.md](API_REFERENCE.md)

---

## Getting Help

If you encounter issues not covered here:

- **GitHub Issues**: [Report a bug](https://github.com/XGraph-Team/SumoXPypsa/issues)
- **Discussions**: [Ask a question](https://github.com/XGraph-Team/SumoXPypsa/discussions)
- **Email**: contact@xgraph-team.com

---

## Update Instructions

To update to the latest version:

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install --upgrade -r requirements.txt

# Restart the application
python main_complete_integration.py
```

---

**Successfully installed? [Back to README](../README.md) | [View Features](FEATURES.md)**
