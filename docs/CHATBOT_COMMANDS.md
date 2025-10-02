# Chatbot Commands Reference

Complete guide to all commands supported by the Ultra-Intelligent AI Chatbot.

---

## Table of Contents

- [Overview](#overview)
- [Vehicle Control](#vehicle-control)
- [Substation Operations](#substation-operations)
- [V2G Operations](#v2g-operations)
- [EV Charging Stations](#ev-charging-stations)
- [Scenario Commands](#scenario-commands)
- [Analytics & Reporting](#analytics--reporting)
- [Map & Visualization](#map--visualization)
- [System Control](#system-control)
- [Natural Language Features](#natural-language-features)

---

## Overview

The Ultra-Intelligent AI Chatbot uses OpenAI GPT to understand natural language commands with:
- **Typo Correction**: Automatically fixes spelling mistakes
- **Intent Recognition**: Understands command variations
- **Context Awareness**: Remembers conversation context
- **Smart Suggestions**: Provides helpful next-step recommendations

### Command Syntax

Commands can be typed in **natural language** - the AI understands variations:

✅ **Formal**: `start vehicles`
✅ **Casual**: `spawn some cars`
✅ **With typos**: `strat veihcles`
✅ **Detailed**: `start 100 vehicles with 80% EVs`

---

## Vehicle Control

### Start Vehicle Simulation

**Basic**:
```
start vehicles
spawn vehicles
create vehicles
launch simulation
```

**With count**:
```
start 50 vehicles
spawn 100 cars
create 200 vehicles
```

**With parameters**:
```
start 100 vehicles with 70% EVs
spawn 50 cars, 80% electric, battery 30-90%
```

**Examples**:
- ✅ `start vehicles` → Spawns 50 vehicles (default)
- ✅ `start 200 vehicles` → Spawns 200 vehicles
- ✅ `strat vehicals` → AI corrects typos, executes command

**Response**:
```
✅ Starting vehicle simulation...
🚗 Spawning 50 vehicles...
✅ Successfully spawned 50 vehicles
```

---

### Highlight Vehicle

**Command**:
```
highlight vehicle_0
track vehicle_42
show me vehicle_123
follow car_15
```

**Examples**:
- ✅ `highlight vehicle_0` → Vehicle highlighted on map with camera focus
- ✅ `track vehicle_42` → Follows vehicle in real-time

**Response**:
```
✅ Highlighting vehicle_0 on the map
🎯 Camera focused on vehicle
```

---

## Substation Operations

### Fail Substation

**Command**:
```
fail Times Square
fail [SUBSTATION_NAME]
trigger failure at Broadway
shut down Times Square substation
```

**Available Substations**:
- Times Square
- Broadway
- Central Park South
- West Side
- East Side
- Midtown
- Columbus Circle
- Lincoln Center

**Examples**:
- ✅ `fail Times Square` → Triggers substation failure
- ✅ `shut down Broadway` → Same as fail command

**Response**:
```
⚠️ Failing Times Square substation...
❌ Times Square is now OFFLINE
🚨 Traffic lights in area turning yellow
⚡ Connected EV stations going offline
```

**Effects**:
- Substation turns red on map
- Traffic lights turn yellow (caution mode)
- Connected EV stations go offline
- Power grid rebalances load

---

### Restore Substation

**Command**:
```
restore Times Square
fix Times Square
bring back Broadway
repair [SUBSTATION_NAME]
turn on Times Square
```

**Examples**:
- ✅ `restore Times Square` → Restores failed substation
- ✅ `fix Broadway` → Same as restore

**Response**:
```
✅ Restoring Times Square substation...
⚡ Times Square is now ONLINE
🟢 Traffic lights resuming normal operation
🔌 Connected EV stations coming online
```

---

### Show Substation Status

**Command**:
```
show substation status
list all substations
substation overview
what's the grid status?
```

**Response**:
```
📊 Substation Status:
✅ Times Square: ONLINE (85% load)
✅ Broadway: ONLINE (72% load)
❌ Central Park South: OFFLINE
✅ West Side: ONLINE (91% load)
...
```

---

## V2G Operations

### Activate V2G

**General activation**:
```
activate v2g
enable v2g
start v2g
turn on vehicle to grid
```

**For specific substation**:
```
activate v2g for Times Square
enable v2g at Broadway
start v2g for [SUBSTATION_NAME]
```

**Examples**:
- ✅ `activate v2g` → Enables V2G for all failed substations
- ✅ `activate v2g for Broadway` → Enables V2G only for Broadway

**Response**:
```
⚡ Activating V2G for Times Square...
🔍 Searching for high-SOC vehicles nearby...
🚗 Found 12 eligible vehicles
📍 Routing vehicles to EV stations...
✅ V2G activated: 12 vehicles providing 3.0 kW
💰 Energy price: $0.15/kWh
```

**V2G Selection Criteria**:
- Battery SOC > 70%
- Within 2km of substation
- Not currently charging
- EV vehicle type

---

### Disable V2G

**Command**:
```
disable v2g
stop v2g
turn off vehicle to grid
deactivate v2g for Times Square
```

**Response**:
```
⚠️ Disabling V2G for Times Square...
🔌 Disconnecting 12 vehicles...
💵 Total earnings distributed: $45.30
✅ V2G disabled
```

---

### V2G Status

**Command**:
```
show v2g status
v2g status
how many vehicles providing power?
v2g overview
```

**Response**:
```
⚡ V2G System Status:

Active Sessions: 12
Total Power: 3.0 kW
Energy Delivered: 25.4 kWh
Total Earnings: $45.30

Active Vehicles:
• vehicle_15: 250W, 2.1 kWh, $3.15
• vehicle_23: 250W, 1.8 kWh, $2.70
• vehicle_42: 250W, 3.4 kWh, $5.10
...
```

---

## EV Charging Stations

### Show Charging Stations Near Substation

**Command**:
```
show charging near Times Square
show ev stations near Broadway
charging stations at [SUBSTATION_NAME]
where can I charge near Times Square?
```

**Examples**:
- ✅ `show charging near Times Square` → Highlights EV stations connected to Times Square
- ✅ `show ev stations near Broadway` → Same result for Broadway

**Response**:
```
🔌 EV Charging Stations near Times Square:

📍 Station 1 (42nd & 7th): 4 chargers, 3 in use
📍 Station 2 (44th & Broadway): 6 chargers, 1 in use
📍 Station 3 (40th & 8th): 4 chargers, all available

✅ 3 stations highlighted on map
```

---

### Show All Charging Stations

**Command**:
```
show all charging stations
list ev stations
where are the chargers?
show all ev stations
```

**Response**:
```
🔌 24 EV Charging Stations in Manhattan:

Times Square Area (8 stations)
Broadway Area (6 stations)
Central Park (5 stations)
Midtown (5 stations)

✅ All stations highlighted on map
```

---

## Scenario Commands

### V2G Emergency Rescue Scenario

**Command**:
```
run v2g scenario
execute v2g scenario
show me v2g demo
v2g emergency scenario
```

**Flow**:
1. **You type**: `run v2g scenario`
2. **AI responds** with scenario description:
   ```
   🎬 V2G EMERGENCY RESCUE SCENARIO

   This scenario demonstrates V2G technology saving the grid:
   1. High-battery vehicles spawn (70-95% SOC)
   2. Times Square substation fails
   3. 18 people trapped in elevators
   4. V2G automatically activates
   5. Vehicles provide emergency power
   6. System stabilizes

   Type 'confirm' to start
   ```
3. **You type**: `confirm`
4. **Cinematic execution**:
   - Camera flies to Times Square
   - Substation fails dramatically
   - Emergency alerts appear
   - V2G system activates
   - Vehicles drive to stations
   - Power is restored
   - Success summary

**Duration**: ~90 seconds

---

### Citywide Blackout Scenario

**Command**:
```
blackout scenario
trigger blackout
citywide blackout scenario
run blackout demo
```

**Flow**:
1. **You type**: `blackout scenario`
2. **AI responds** with description:
   ```
   🎬 CITYWIDE BLACKOUT SCENARIO

   Simulates cascading grid failure:
   1. Low-battery vehicles spawn (25-35% SOC)
   2. Multiple substations fail in sequence
   3. Widespread power outage
   4. Emergency response activated
   5. V2G helps stabilize grid
   6. Gradual recovery

   Type 'confirm' to start
   ```
3. **You type**: `confirm`
4. **Cinematic execution**:
   - Camera shows Manhattan overview
   - Substations fail in cascade
   - Map darkens
   - Emergency protocols activate
   - V2G provides critical power
   - Gradual restoration

**Duration**: ~2 minutes

---

### Confirm Scenario

**Command**:
```
confirm
yes
proceed
start
go ahead
```

**Use**: After being prompted to confirm a scenario

---

## Analytics & Reporting

### Grid Analysis

**Command**:
```
analyze grid
grid analysis
how is the grid performing?
show me grid insights
```

**Response**:
```
🧠 AI Grid Analysis:

Overall Status: HEALTHY
Active Substations: 7/8
Total Load: 45.2 MW
Average Loading: 78%

⚠️ Concerns:
• West Side substation at 91% (near capacity)
• Central Park South offline

💡 Recommendations:
• Consider load shedding for West Side
• Restore Central Park South soon
• V2G available if needed (12 vehicles ready)
```

---

### Demand Prediction

**Command**:
```
predict demand
show demand forecast
what will demand be?
ml prediction
```

**Response**:
```
📈 ML Demand Prediction (Next 6 hours):

Current: 45.2 MW
+1h: 48.1 MW (+6%)
+3h: 52.3 MW (+16%)
+6h: 49.7 MW (+10%)

Peak expected: 3:00 PM (52.3 MW)
Confidence: 94%
Model: LSTM Neural Network
```

---

### System Status

**Command**:
```
system status
status report
how's everything?
give me an overview
```

**Response**:
```
📊 System Status Report:

🚗 Vehicles: 87 total (61 EVs, 26 ICE)
⚡ Substations: 7/8 online (87.5%)
🔋 V2G: Inactive (12 vehicles ready)
🔌 Charging: 8 vehicles charging
📊 Grid Load: 45.2 MW (78% avg)
⚙️ Performance: 87 FPS, 4ms update

✅ System Health: GOOD
```

---

## Map & Visualization

### Show on Map

**Command**:
```
show Times Square on map
zoom to Broadway
focus on Central Park
show me [LOCATION]
```

**Examples**:
- ✅ `show Times Square on map` → Camera moves to Times Square
- ✅ `zoom to Broadway` → Zooms to Broadway area

---

### Toggle Map Layers

**Command**:
```
show substations
hide ev stations
toggle traffic lights
show vehicle routes
```

**Available Layers**:
- Substations
- EV Charging Stations
- Traffic Lights
- Vehicle Labels
- Routes

---

## System Control

### Reset System

**Command**:
```
reset system
restart simulation
clear all vehicles
reset everything
```

**Response**:
```
⚠️ Resetting system...
🗑️ Removing all vehicles
🔄 Restoring all substations
📊 Clearing statistics
✅ System reset complete
```

---

### Stop Simulation

**Command**:
```
stop simulation
pause vehicles
stop sumo
halt traffic
```

---

## Natural Language Features

### Typo Correction

The AI automatically corrects common typos:

- `strat vehicels` → `start vehicles` ✅
- `faill Times Sqaure` → `fail Times Square` ✅
- `activ8 v2g` → `activate v2g` ✅
- `show chargng staions` → `show charging stations` ✅

### Intent Recognition

The AI understands various phrasings:

**Same intent, different phrases**:
- `start vehicles` = `spawn cars` = `create traffic` = `launch simulation`
- `fail Times Square` = `shut down Times Square` = `kill Times Square power`
- `activate v2g` = `enable vehicle to grid` = `turn on v2g`

### Contextual Understanding

The AI remembers context:

**Example conversation**:
```
You: fail Times Square
AI: ✅ Times Square failed

You: now activate v2g
AI: ✅ Activating V2G for Times Square (understands "for Times Square" from context)

You: how many vehicles?
AI: 12 vehicles providing 3.0 kW (understands you're asking about V2G)
```

---

## Command Cheat Sheet

### Quick Reference

| Category | Command | Result |
|----------|---------|--------|
| **Vehicles** | `start vehicles` | Spawn 50 vehicles |
| | `start 100 vehicles` | Spawn 100 vehicles |
| | `highlight vehicle_0` | Highlight vehicle |
| **Substations** | `fail Times Square` | Trigger failure |
| | `restore Times Square` | Restore substation |
| **V2G** | `activate v2g` | Enable V2G |
| | `show v2g status` | V2G statistics |
| **Charging** | `show charging near [SUB]` | Show EV stations |
| **Scenarios** | `run v2g scenario` | V2G demo |
| | `blackout scenario` | Blackout demo |
| | `confirm` | Start scenario |
| **Analytics** | `analyze grid` | AI analysis |
| | `predict demand` | ML forecast |
| | `system status` | Full report |

---

## Tips & Best Practices

### 1. Use Natural Language
Don't worry about exact syntax - the AI understands variations:
```
✅ "Can you start some vehicles please?"
✅ "I need to fail the Times Square substation"
✅ "Show me what's happening with V2G"
```

### 2. Be Specific When Needed
For better results, provide details:
```
✅ "start 200 vehicles with 80% electric"
✅ "activate v2g for Times Square only"
✅ "show charging stations near Broadway"
```

### 3. Ask Questions
The AI can answer questions about the system:
```
✅ "How many vehicles are charging?"
✅ "Which substations are offline?"
✅ "What's the current grid load?"
```

### 4. Use Scenarios for Demos
Scenarios provide cinematic demonstrations:
```
✅ "run v2g scenario" → Full automated demo
✅ "blackout scenario" → Cascading failure demo
```

### 5. Follow Suggestions
The AI provides helpful next steps:
```
AI: "✅ Vehicles spawned. Try 'fail Times Square' or 'run v2g scenario'"
```

---

## Troubleshooting

### Command Not Recognized

**Issue**: AI doesn't understand your command

**Solutions**:
- Try rephrasing: `"start cars"` instead of `"begin vehicle simulation"`
- Check spelling: AI corrects typos but extreme errors may fail
- Use simpler language: `"fail Times Square"` instead of `"initiate substation failure sequence"`

### No Response

**Issue**: Chatbot doesn't respond

**Solutions**:
- Check OpenAI API key in `.env`
- Verify internet connection
- Check browser console (F12) for errors
- Restart the application

### Wrong Command Executed

**Issue**: AI executes different command than intended

**Solutions**:
- Be more specific: `"activate v2g for Times Square"` not just `"activate"`
- Check response before confirming scenarios
- Provide context: `"show v2g status for Times Square"`

---

## Advanced Usage

### Chaining Commands

You can describe multi-step operations:
```
"Start 100 vehicles, then fail Times Square, and activate V2G"
```

The AI will execute in sequence.

### Conditional Commands

The AI understands conditions:
```
"If West Side is above 90% load, activate V2G"
"Show me EVs with battery above 80%"
```

---

## Keyboard Shortcuts

While using the chatbot:

- **Enter**: Send message
- **Shift+Enter**: New line
- **Esc**: Close chatbot
- **Ctrl+L**: Clear chat history (focus chatbot first)

---

## API Integration

For programmatic access, use the API instead:

```python
import requests

response = requests.post('http://localhost:5000/api/ai/chat', json={
    'message': 'start 100 vehicles',
    'user_id': 'operator_1'
})

print(response.json())
```

See [API_REFERENCE.md](API_REFERENCE.md) for details.

---

## Examples Gallery

### Example 1: Quick Vehicle Test
```
You: start 50 vehicles
AI: ✅ Starting vehicle simulation... 50 vehicles spawned

You: highlight vehicle_0
AI: ✅ Vehicle_0 highlighted on map
```

### Example 2: Substation Failure & V2G
```
You: fail Times Square
AI: ⚠️ Times Square substation failed

You: activate v2g
AI: ⚡ V2G activated, 12 vehicles providing 3.0 kW
```

### Example 3: Full Scenario
```
You: run v2g scenario
AI: 🎬 V2G EMERGENCY RESCUE SCENARIO... Type 'confirm' to start

You: confirm
AI: ✅ Starting scenario... [Cinematic presentation runs]
```

### Example 4: Analytics
```
You: how is the grid doing?
AI: 📊 Grid Status: 7/8 substations online, 78% average load, all systems healthy

You: predict demand
AI: 📈 Next 6h: Peak at 3 PM (52.3 MW), confidence 94%
```

---

**Questions?** [Open an issue](https://github.com/XGraph-Team/SumoXPypsa/issues) | [Back to README](../README.md)
