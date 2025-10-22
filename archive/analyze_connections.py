#!/usr/bin/env python3
import requests
import json

# Get network state
response = requests.get('http://localhost:5000/api/network_state')
network_state = response.json()

print("=== TIMES SQUARE CONNECTION ANALYSIS ===")

# Analyze primary cables from Times Square
print("\n1. PRIMARY CABLES FROM TIMES SQUARE:")
times_square_primary = [cable for cable in network_state['cables']['primary'] if cable['from'] == 'Times Square']
print(f"Found {len(times_square_primary)} primary cables")
for cable in times_square_primary[:5]:  # Show first 5
    print(f"  - {cable['id']}: {cable['from']} -> {cable['to']}")

# Analyze secondary cables for Times Square
print("\n2. SECONDARY CABLES FOR TIMES SQUARE:")
times_square_secondary = [cable for cable in network_state['cables']['secondary'] if cable.get('substation') == 'Times Square']
print(f"Found {len(times_square_secondary)} secondary cables")
for cable in times_square_secondary[:5]:  # Show first 5
    print(f"  - {cable['id']}: {cable['from']} -> {cable['to']} (substation: {cable.get('substation', 'N/A')})")

# Analyze EV stations
print("\n3. EV STATIONS CONNECTED TO TIMES SQUARE:")
connected_ev_ids = []
for cable in times_square_secondary:
    if cable.get('to'):
        for ev in network_state['ev_stations']:
            if ev['id'] == cable['to'] or ev.get('traffic_light_id') == cable['to']:
                connected_ev_ids.append(ev['id'])
                print(f"  - EV {ev['id']} connected via cable {cable['id']}")

print(f"\nTotal connected EVs: {len(set(connected_ev_ids))}")

# Check how the data is structured in map layers
print("\n4. SAMPLE CABLE DATA STRUCTURE:")
if times_square_primary:
    sample = times_square_primary[0]
    print(f"Sample primary cable: {json.dumps(sample, indent=2)}")

if times_square_secondary:
    sample = times_square_secondary[0]
    print(f"Sample secondary cable: {json.dumps(sample, indent=2)}")