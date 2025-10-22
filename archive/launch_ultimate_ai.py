#!/usr/bin/env python3
"""
Launch script for the ULTIMATE AI Controller
Fixes Windows Unicode issues and provides clean output
"""

import sys
import os
sys.path.append('.')

from flask import Flask, jsonify
from ultimate_ai_controller import initialize_ultimate_ai
from core.power_system import ManhattanPowerGrid
from integrated_backend import ManhattanIntegratedSystem
from ml_engine import MLPowerGridEngine
from enhanced_v2g_manager import initialize_enhanced_v2g
import asyncio

# Global AI controller instance
ai_controller = None
integrated_system = None

app = Flask(__name__)

def initialize_systems():
    global ai_controller, integrated_system

    print("Initializing ULTIMATE AI systems...")

    # Initialize basic systems
    power_grid = ManhattanPowerGrid()
    integrated_system = ManhattanIntegratedSystem(power_grid)
    ml_engine = MLPowerGridEngine(power_grid, integrated_system)

    # Initialize ENHANCED V2G system
    v2g_manager = initialize_enhanced_v2g(integrated_system)

    # Initialize ULTIMATE AI controller with enhanced V2G
    ai_controller = initialize_ultimate_ai(integrated_system, ml_engine, v2g_manager, app)

    if ai_controller:
        print("[SUCCESS] ULTIMATE AI Controller initialized successfully")
    else:
        print("[ERROR] AI Controller failed to initialize")

@app.route('/test_ai')
def test_ai():
    """Test dynamic AI functionality"""
    try:
        if not ai_controller:
            return jsonify({'status': 'error', 'message': 'AI controller not initialized'})

        response = asyncio.run(ai_controller.process_intelligent_command('hi, show me your maximum capabilities'))
        return jsonify({'status': 'success', 'response': response})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/test_map')
def test_map():
    """Test map focus functionality"""
    try:
        if not ai_controller:
            return jsonify({'status': 'error', 'message': 'AI controller not initialized'})

        response = asyncio.run(ai_controller.process_intelligent_command('show me times square on the map with full detail'))
        return jsonify({'status': 'success', 'response': response})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/test_v2g')
def test_v2g():
    """Test V2G activation"""
    try:
        if not ai_controller:
            return jsonify({'status': 'error', 'message': 'AI controller not initialized'})

        response = asyncio.run(ai_controller.process_intelligent_command('activate all V2G vehicles and show me the status'))
        return jsonify({'status': 'success', 'response': response})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/test_system_analysis')
def test_system_analysis():
    """Test comprehensive system analysis"""
    try:
        if not ai_controller:
            return jsonify({'status': 'error', 'message': 'AI controller not initialized'})

        response = asyncio.run(ai_controller.process_intelligent_command('analyze the entire Manhattan power grid and give me comprehensive insights with predictions'))
        return jsonify({'status': 'success', 'response': response})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'ai_initialized': ai_controller is not None,
        'system_initialized': integrated_system is not None,
        'ultimate_ai_active': True
    })

if __name__ == '__main__':
    print("=" * 60)
    print("ULTIMATE AI CONTROLLER - MAXIMUM INTELLIGENCE")
    print("True AI that actually controls everything")
    print("=" * 60)

    # Initialize all systems first
    initialize_systems()

    print("\\nStarting ULTIMATE AI server on http://localhost:5002")
    print("\\nTest Endpoints:")
    print("* /health - System health check")
    print("* /test_ai - Test maximum AI capabilities")
    print("* /test_map - Test dynamic map control")
    print("* /test_v2g - Test V2G activation")
    print("* /test_system_analysis - Test system analysis")
    print("\\n" + "=" * 60)
    print("READY FOR ULTIMATE AI TESTING!")
    print("=" * 60)

    app.run(host='127.0.0.1', port=5002, debug=False)