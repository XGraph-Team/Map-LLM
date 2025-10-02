# Project Structure - Manhattan Power Grid

Clean, organized project structure ready for GitHub release.

---

## 📁 Main Directory Structure

```
SumoXPypsa/
│
├── 📄 Core Files
│   ├── main_complete_integration.py     # Main Flask application (entry point)
│   ├── ultra_intelligent_chatbot.py     # AI chatbot with OpenAI integration
│   ├── v2g_manager.py                   # Vehicle-to-Grid energy management
│   ├── ml_engine.py                     # Machine learning analytics
│   ├── manhattan_sumo_manager.py        # SUMO traffic simulation manager
│   ├── ev_battery_model.py              # EV battery simulation
│   ├── ev_station_manager.py            # Charging station management
│   └── index.html                       # Main web interface
│
├── 📚 Documentation
│   ├── README.md                        # Main project README (world-class)
│   ├── CONTRIBUTING.md                  # Contribution guidelines
│   ├── PERFORMANCE_OPTIMIZATIONS.md     # Performance documentation
│   ├── GITHUB_READY.md                  # GitHub release checklist
│   └── PROJECT_STRUCTURE.md             # This file
│
├── 📁 docs/                             # Detailed documentation
│   ├── INSTALLATION.md                  # Complete setup guide
│   ├── CHATBOT_COMMANDS.md              # All chatbot commands reference
│   └── images/                          # Screenshots (add your own)
│
├── 📁 static/                           # Frontend assets
│   ├── script.js                        # Main application logic
│   ├── styles.css                       # Glassmorphic UI styling
│   ├── scenario-director.js             # Scenario orchestration
│   ├── chatbot-scenarios.js             # Chatbot-scenario integration
│   └── performance-monitor.js           # FPS & metrics tracking
│
├── 📁 core/                             # Core system modules
│   ├── sumo_manager.py                  # SUMO integration
│   └── power_system.py                  # PyPSA power grid
│
├── 📁 data/                             # Data files
│   ├── manhattan.osm                    # OpenStreetMap data
│   ├── manhattan.net.xml                # SUMO network definition
│   ├── substations.json                 # Substation locations & data
│   └── ev_stations.json                 # EV charging station data
│
├── 📁 config/                           # Configuration files
│   └── (vehicle/grid configuration files)
│
├── 📁 scripts/                          # Utility scripts
│   └── (setup and utility scripts)
│
├── 📁 monitoring/                       # Monitoring & logging
│   └── (monitoring configuration)
│
├── 📁 archive/                          # Archived/reference files
│   ├── wsdm2026_llm_to_map.tex         # Research paper LaTeX
│   ├── wsdm2026_llm_to_map_FINAL.tex   # Research paper LaTeX
│   ├── wsdm2026_llm_to_map_HONEST.tex  # Research paper LaTeX
│   ├── z.tex                            # LaTeX draft
│   ├── references.bib                   # Bibliography
│   ├── ai_advanced_modules.py           # Old AI module
│   ├── integrated_backend.py            # Old backend
│   └── enhanced_v2g_manager.py          # Old V2G module
│
├── 🔧 Configuration
│   ├── .gitignore                       # Git ignore rules
│   ├── .env.example                     # Environment template
│   ├── requirements.txt                 # Python dependencies
│   ├── LICENSE                          # MIT License
│   └── docker-compose.yml               # Docker configuration (if needed)
│
└── 📁 logs/                             # Application logs (gitignored)
    └── (runtime logs)
```

---

## 🗂️ File Categories

### Active Production Files

**Core Application** ✅
- `main_complete_integration.py` - Main Flask app, all API endpoints
- `ultra_intelligent_chatbot.py` - AI chatbot with OpenAI, command processing
- `v2g_manager.py` - V2G operations, vehicle-to-grid management
- `ml_engine.py` - Machine learning demand prediction
- `manhattan_sumo_manager.py` - SUMO simulation control
- `ev_battery_model.py` - Battery state modeling
- `ev_station_manager.py` - Charging station operations

**Frontend** ✅
- `index.html` - Main web interface
- `static/script.js` - Core application logic (WebGL, Map, Data)
- `static/styles.css` - UI styling (glassmorphic design)
- `static/scenario-director.js` - Scenario system
- `static/chatbot-scenarios.js` - Chatbot integration

**Documentation** ✅
- `README.md` - Main project documentation
- `docs/INSTALLATION.md` - Setup guide
- `docs/CHATBOT_COMMANDS.md` - Command reference
- `CONTRIBUTING.md` - How to contribute
- `PERFORMANCE_OPTIMIZATIONS.md` - Performance details
- `GITHUB_READY.md` - Release checklist

**Configuration** ✅
- `.gitignore` - Git exclusions
- `.env.example` - Environment template
- `requirements.txt` - Dependencies
- `LICENSE` - MIT License

### Archived Files (Not in Active Use)

Moved to `archive/` folder for reference:
- LaTeX research papers
- Old/unused Python modules
- Bibliography files

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/XGraph-Team/SumoXPypsa.git
   cd SumoXPypsa
   ```

2. **Install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application**
   ```bash
   python main_complete_integration.py
   ```

5. **Open browser**
   ```
   http://localhost:5000
   ```

See [docs/INSTALLATION.md](docs/INSTALLATION.md) for detailed instructions.

---

## 📊 File Count Summary

| Category | Count | Status |
|----------|-------|--------|
| **Core Python Files** | 7 | ✅ Active |
| **Frontend Files** | 5 | ✅ Active |
| **Documentation** | 6 | ✅ Complete |
| **Configuration** | 4 | ✅ Complete |
| **Data Files** | 4 | ✅ Active |
| **Archived** | ~10 | 📦 Reference |

**Total Active Files**: ~26 essential files
**Status**: Clean, organized, production-ready ✅

---

## 🧹 Cleanup Summary

### Deleted Files (No Longer Needed)
- ❌ 19 temporary documentation files (FINAL_*, CRITICAL_*, QUICK_FIX*, etc.)
- ❌ 9 test/debug Python files (test_*.py, debug_*.py)
- ❌ 9 backup/old AI files (*_BACKUP_*.py, old chatbot versions)
- ❌ 4 log files (server*.log)
- ❌ 1 duplicate file (CHAT_COMMANDS.md - now in docs/)

**Total Deleted**: 42 unnecessary files

### Archived Files (Kept for Reference)
- 📦 4 LaTeX research papers moved to `archive/`
- 📦 1 bibliography file moved to `archive/`
- 📦 3 unused Python modules moved to `archive/`

**Total Archived**: 8 reference files

---

## 🎯 Key Features by File

### Main Application (`main_complete_integration.py`)
- Flask web server
- All API endpoints
- SUMO integration
- PyPSA power grid
- V2G management
- AI chatbot routing
- Real-time data streaming

### AI Chatbot (`ultra_intelligent_chatbot.py`)
- OpenAI GPT integration
- Natural language processing
- Command intent detection
- Typo correction
- Scenario delegation
- Context awareness

### V2G Manager (`v2g_manager.py`)
- Vehicle selection algorithm
- Energy trading
- Automatic routing
- Revenue calculation
- Session management
- Emergency response

### Frontend (`static/script.js`)
- WebGL GPU rendering
- Mapbox map integration
- Real-time updates
- Performance monitoring
- Vehicle visualization
- Interactive controls

### Scenario System (`static/scenario-director.js`)
- V2G emergency rescue
- Citywide blackout
- Camera automation
- Narration system
- Event orchestration

---

## 🔍 Important Notes

### Files to Keep Updated
1. **README.md** - Add demo video link when available
2. **requirements.txt** - Update versions as needed
3. **.env.example** - Add new config options
4. **docs/INSTALLATION.md** - Update for platform changes

### Files Created at Runtime (gitignored)
- `manhattan_grid.db` - SQLite database
- `logs/*.log` - Application logs
- `*.pyc` - Python bytecode
- `__pycache__/` - Python cache

### External Dependencies
- **SUMO** - Must be installed separately
- **OpenAI API Key** - Required for chatbot
- **Mapbox Token** - Required for maps

---

## 📝 Next Steps

1. ✅ Project structure is clean and organized
2. ✅ All unnecessary files removed
3. ✅ Documentation complete
4. 📸 Add screenshots to `docs/images/`
5. 🎬 Record demo video and update README.md
6. 🚀 Push to GitHub: `git push origin main`
7. 🌟 Share with the world!

---

**Built with ❤️ by XGraph Team**

For questions: [GitHub Issues](https://github.com/XGraph-Team/SumoXPypsa/issues)
