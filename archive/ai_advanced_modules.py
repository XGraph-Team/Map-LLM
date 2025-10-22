"""
Advanced AI Modules for World-Class Manhattan Power Grid Chatbot
Research-level components for visual processing, pattern analysis, and intelligent interaction
"""

import json
import numpy as np
import threading
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from collections import defaultdict, deque
from dataclasses import dataclass, field
import logging
import hashlib
import statistics

try:
    import cv2
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    cv2 = None
    Image = ImageDraw = ImageFont = None

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class VisualProcessor:
    """Advanced visual processing for map analysis and system visualization"""

    def __init__(self):
        self.enabled = cv2 is not None
        self.analysis_cache = {}
        self.map_state_history = deque(maxlen=100)

        if self.enabled:
            print("Visual Processor initialized with computer vision capabilities")
        else:
            print("Visual Processor initialized without OpenCV (limited functionality)")

    def analyze_map_state(self, map_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze current map state and extract insights"""
        try:
            analysis = {
                "timestamp": datetime.now().isoformat(),
                "grid_health_visual": self._analyze_grid_health(map_data),
                "traffic_flow_patterns": self._analyze_traffic_patterns(map_data),
                "charging_station_utilization": self._analyze_charging_stations(map_data),
                "anomalies_detected": self._detect_visual_anomalies(map_data),
                "optimization_opportunities": self._identify_optimization_areas(map_data)
            }

            # Store in history for trend analysis
            self.map_state_history.append(analysis)

            return analysis
        except Exception as e:
            return {"error": f"Visual analysis failed: {str(e)}"}

    def _analyze_grid_health(self, map_data: Dict) -> Dict[str, Any]:
        """Analyze power grid health from visual data"""
        substations = map_data.get("substations", [])
        operational = sum(1 for s in substations if s.get("operational", False))
        total = len(substations)

        return {
            "health_score": (operational / max(total, 1)) * 100,
            "operational_substations": operational,
            "total_substations": total,
            "critical_areas": [s["name"] for s in substations if not s.get("operational", False)],
            "load_distribution": self._analyze_load_distribution(substations)
        }

    def _analyze_traffic_patterns(self, map_data: Dict) -> Dict[str, Any]:
        """Analyze traffic flow patterns"""
        vehicles = map_data.get("vehicles", [])
        if not vehicles:
            return {"pattern": "no_traffic", "density": 0}

        # Analyze vehicle distribution and movement patterns
        speeds = [v.get("speed", 0) for v in vehicles]
        positions = [(v.get("lat", 0), v.get("lon", 0)) for v in vehicles]

        return {
            "vehicle_count": len(vehicles),
            "average_speed": statistics.mean(speeds) if speeds else 0,
            "speed_variance": statistics.variance(speeds) if len(speeds) > 1 else 0,
            "density_hotspots": self._identify_density_hotspots(positions),
            "congestion_level": self._calculate_congestion_level(speeds)
        }

    def _analyze_charging_stations(self, map_data: Dict) -> Dict[str, Any]:
        """Analyze EV charging station utilization"""
        ev_stations = map_data.get("ev_stations", [])

        total_capacity = sum(station.get("total_ports", 0) for station in ev_stations)
        total_occupied = sum(station.get("vehicles_charging", 0) for station in ev_stations)

        return {
            "utilization_rate": (total_occupied / max(total_capacity, 1)) * 100,
            "stations_at_capacity": len([s for s in ev_stations if s.get("vehicles_charging", 0) >= s.get("total_ports", 1)]),
            "available_capacity": total_capacity - total_occupied,
            "peak_demand_stations": sorted(ev_stations, key=lambda x: x.get("vehicles_charging", 0), reverse=True)[:3]
        }

    def _detect_visual_anomalies(self, map_data: Dict) -> List[Dict[str, Any]]:
        """Detect visual anomalies in the system"""
        anomalies = []

        # Check for unusual patterns
        if len(self.map_state_history) > 10:
            recent_states = list(self.map_state_history)[-10:]

            # Detect sudden changes in grid health
            health_scores = [state.get("grid_health_visual", {}).get("health_score", 100) for state in recent_states]
            if len(health_scores) > 1:
                health_change = health_scores[-1] - statistics.mean(health_scores[:-1])
                if abs(health_change) > 20:
                    anomalies.append({
                        "type": "grid_health_change",
                        "severity": "HIGH" if abs(health_change) > 50 else "MEDIUM",
                        "description": f"Grid health changed by {health_change:.1f}%",
                        "timestamp": datetime.now().isoformat()
                    })

        return anomalies

    def _identify_optimization_areas(self, map_data: Dict) -> List[str]:
        """Identify areas for optimization"""
        opportunities = []

        # Check for underutilized charging stations
        ev_stations = map_data.get("ev_stations", [])
        underutilized = [s for s in ev_stations if s.get("vehicles_charging", 0) == 0 and s.get("operational", False)]
        if len(underutilized) > 2:
            opportunities.append(f"Redirect vehicles to {len(underutilized)} underutilized charging stations")

        # Check for traffic congestion
        vehicles = map_data.get("vehicles", [])
        slow_vehicles = [v for v in vehicles if v.get("speed", 0) < 1.0]
        if len(slow_vehicles) > len(vehicles) * 0.3:
            opportunities.append("High traffic congestion detected - optimize signal timing")

        return opportunities

    def _identify_density_hotspots(self, positions: List[Tuple[float, float]]) -> List[Dict[str, float]]:
        """Identify traffic density hotspots"""
        if not positions:
            return []

        # Simple density clustering
        hotspots = []
        threshold = 0.001  # Approximate distance threshold

        for lat, lon in positions:
            nearby = sum(1 for plat, plon in positions
                        if abs(plat - lat) < threshold and abs(plon - lon) < threshold)
            if nearby > 5:  # Hotspot threshold
                hotspots.append({"lat": lat, "lon": lon, "density": nearby})

        return sorted(hotspots, key=lambda x: x["density"], reverse=True)[:5]

    def _calculate_congestion_level(self, speeds: List[float]) -> str:
        """Calculate overall congestion level"""
        if not speeds:
            return "unknown"

        avg_speed = statistics.mean(speeds)
        if avg_speed < 2.0:
            return "high"
        elif avg_speed < 5.0:
            return "moderate"
        else:
            return "low"

    def _analyze_load_distribution(self, substations: List[Dict]) -> Dict[str, Any]:
        """Analyze power load distribution across substations"""
        if not substations:
            return {"balanced": True, "variance": 0}

        loads = [s.get("load_mw", 0) for s in substations if s.get("operational", False)]
        if not loads:
            return {"balanced": True, "variance": 0}

        mean_load = statistics.mean(loads)
        variance = statistics.variance(loads) if len(loads) > 1 else 0

        return {
            "balanced": variance < (mean_load * 0.2),  # Within 20% of mean
            "variance": variance,
            "mean_load": mean_load,
            "load_imbalance_score": variance / max(mean_load, 1)
        }


class PatternAnalyzer:
    """Advanced pattern recognition and trend analysis"""

    def __init__(self):
        self.historical_patterns = defaultdict(list)
        self.trend_cache = {}
        self.pattern_library = self._build_pattern_library()

    def _build_pattern_library(self) -> Dict[str, Any]:
        """Build library of known system patterns"""
        return {
            "power_demand_patterns": {
                "morning_peak": {"hours": [7, 8, 9], "multiplier": 1.3},
                "evening_peak": {"hours": [17, 18, 19], "multiplier": 1.4},
                "weekend_low": {"days": [6, 0], "multiplier": 0.8}
            },
            "traffic_patterns": {
                "rush_hour": {"hours": [8, 17, 18], "congestion_factor": 2.0},
                "lunch_peak": {"hours": [12, 13], "congestion_factor": 1.2}
            },
            "charging_patterns": {
                "workplace_charging": {"hours": [9, 10, 11, 14, 15, 16], "demand": "high"},
                "home_charging": {"hours": [20, 21, 22, 23], "demand": "very_high"}
            }
        }

    def analyze_system_patterns(self, system_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze patterns in system behavior"""
        current_time = datetime.now()

        patterns = {
            "timestamp": current_time.isoformat(),
            "detected_patterns": self._detect_active_patterns(system_data, current_time),
            "trend_analysis": self._analyze_trends(system_data),
            "predictive_insights": self._generate_predictive_insights(system_data, current_time),
            "anomaly_score": self._calculate_anomaly_score(system_data),
            "optimization_recommendations": self._generate_pattern_based_recommendations(system_data)
        }

        # Store for future analysis
        self.historical_patterns[current_time.date()].append(patterns)

        return patterns

    def _detect_active_patterns(self, system_data: Dict, current_time: datetime) -> List[Dict[str, Any]]:
        """Detect currently active patterns"""
        active_patterns = []
        current_hour = current_time.hour
        current_day = current_time.weekday()

        # Check power demand patterns
        for pattern_name, pattern_info in self.pattern_library["power_demand_patterns"].items():
            if "hours" in pattern_info and current_hour in pattern_info["hours"]:
                active_patterns.append({
                    "type": "power_demand",
                    "name": pattern_name,
                    "confidence": 0.9,
                    "expected_impact": pattern_info.get("multiplier", 1.0)
                })
            elif "days" in pattern_info and current_day in pattern_info["days"]:
                active_patterns.append({
                    "type": "power_demand",
                    "name": pattern_name,
                    "confidence": 0.8,
                    "expected_impact": pattern_info.get("multiplier", 1.0)
                })

        return active_patterns

    def _analyze_trends(self, system_data: Dict) -> Dict[str, Any]:
        """Analyze system trends"""
        ml_data = system_data.get("ml_data", {})
        v2g_data = system_data.get("v2g_data", {})

        return {
            "demand_trend": self._calculate_trend(ml_data.get("recent_demand", [])),
            "v2g_adoption_trend": self._calculate_trend(v2g_data.get("daily_sessions", [])),
            "system_efficiency_trend": self._calculate_efficiency_trend(system_data),
            "prediction_accuracy_trend": self._calculate_trend(ml_data.get("accuracy_history", []))
        }

    def _calculate_trend(self, data_points: List[float]) -> Dict[str, Any]:
        """Calculate trend direction and strength"""
        if len(data_points) < 2:
            return {"direction": "stable", "strength": 0.0, "confidence": 0.0}

        # Simple linear regression
        x = list(range(len(data_points)))
        y = data_points

        n = len(data_points)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(xi * xi for xi in x)

        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x) if (n * sum_x2 - sum_x * sum_x) != 0 else 0

        direction = "increasing" if slope > 0.1 else "decreasing" if slope < -0.1 else "stable"
        strength = abs(slope)
        confidence = min(1.0, strength * 10)  # Confidence based on slope strength

        return {
            "direction": direction,
            "strength": strength,
            "confidence": confidence,
            "slope": slope
        }

    def _calculate_efficiency_trend(self, system_data: Dict) -> Dict[str, Any]:
        """Calculate system efficiency trend"""
        stats = system_data.get("system_stats", {})

        operational_ratio = stats.get("substations_operational", 0) / max(stats.get("total_substations", 1), 1)
        charging_efficiency = stats.get("ev_stations_operational", 0) / max(stats.get("total_ev_stations", 1), 1)

        overall_efficiency = (operational_ratio + charging_efficiency) / 2

        return {
            "current_efficiency": overall_efficiency * 100,
            "operational_ratio": operational_ratio * 100,
            "charging_efficiency": charging_efficiency * 100,
            "trend": "stable"  # Would need historical data for real trend
        }

    def _generate_predictive_insights(self, system_data: Dict, current_time: datetime) -> List[str]:
        """Generate predictive insights based on patterns"""
        insights = []
        current_hour = current_time.hour

        # Predict upcoming demand based on time patterns
        if 6 <= current_hour <= 8:
            insights.append("Morning peak demand expected within 1-2 hours - prepare V2G resources")
        elif 16 <= current_hour <= 17:
            insights.append("Evening peak approaching - optimize charging schedules")

        # Weekend patterns
        if current_time.weekday() == 4:  # Friday
            insights.append("Weekend traffic patterns will begin - adjust charging station priorities")

        return insights

    def _calculate_anomaly_score(self, system_data: Dict) -> float:
        """Calculate overall system anomaly score (0-1)"""
        anomalies = system_data.get("ml_data", {}).get("anomalies", [])
        if not anomalies:
            return 0.0

        # Weight anomalies by severity
        severity_weights = {"LOW": 0.1, "MEDIUM": 0.5, "HIGH": 1.0}

        total_score = sum(severity_weights.get(anomaly.get("severity", "LOW"), 0.1) for anomaly in anomalies)
        normalized_score = min(1.0, total_score / 10)  # Normalize to 0-1

        return normalized_score

    def _generate_pattern_based_recommendations(self, system_data: Dict) -> List[str]:
        """Generate optimization recommendations based on detected patterns"""
        recommendations = []

        anomaly_score = self._calculate_anomaly_score(system_data)
        if anomaly_score > 0.5:
            recommendations.append("High anomaly score detected - investigate system irregularities")

        # V2G optimization based on patterns
        v2g_data = system_data.get("v2g_data", {})
        if v2g_data.get("active_sessions", 0) == 0 and anomaly_score > 0.3:
            recommendations.append("Consider activating V2G to address system anomalies")

        return recommendations


class PredictionEngine:
    """Advanced prediction engine for system behavior"""

    def __init__(self, ml_engine):
        self.ml_engine = ml_engine
        self.prediction_cache = {}
        self.confidence_tracker = defaultdict(list)

    def predict_system_state(self, horizon_minutes: int = 60) -> Dict[str, Any]:
        """Predict system state over specified time horizon"""
        cache_key = f"system_state_{horizon_minutes}"

        if cache_key in self.prediction_cache:
            cached = self.prediction_cache[cache_key]
            if (datetime.now() - cached["timestamp"]).seconds < 300:  # 5 minute cache
                return cached["data"]

        predictions = {
            "timestamp": datetime.now().isoformat(),
            "horizon_minutes": horizon_minutes,
            "power_demand": self._predict_power_demand(horizon_minutes),
            "traffic_flow": self._predict_traffic_flow(horizon_minutes),
            "v2g_opportunities": self._predict_v2g_opportunities(horizon_minutes),
            "grid_stability": self._predict_grid_stability(horizon_minutes),
            "optimization_windows": self._identify_optimization_windows(horizon_minutes)
        }

        self.prediction_cache[cache_key] = {
            "data": predictions,
            "timestamp": datetime.now()
        }

        return predictions

    def _predict_power_demand(self, horizon_minutes: int) -> Dict[str, Any]:
        """Predict power demand over time horizon"""
        if self.ml_engine:
            try:
                ml_predictions = self.ml_engine.predict_power_demand(next_hours=horizon_minutes//60)
                return {
                    "predictions": ml_predictions,
                    "confidence": 0.85,
                    "method": "ml_model"
                }
            except Exception as e:
                pass

        # Fallback to pattern-based prediction
        current_hour = datetime.now().hour
        base_demand = 50 + (current_hour - 12) ** 2 * 0.5  # Parabolic pattern

        return {
            "predictions": [{"hour": i, "predicted_mw": base_demand + i * 2} for i in range(horizon_minutes//60 + 1)],
            "confidence": 0.6,
            "method": "pattern_based"
        }

    def _predict_traffic_flow(self, horizon_minutes: int) -> Dict[str, Any]:
        """Predict traffic flow patterns"""
        current_time = datetime.now()
        predictions = []

        for i in range(0, horizon_minutes, 15):  # 15-minute intervals
            future_time = current_time + timedelta(minutes=i)
            hour = future_time.hour

            # Simple traffic pattern model
            if 7 <= hour <= 9 or 17 <= hour <= 19:
                congestion_level = "high"
                flow_rate = 0.3
            elif 11 <= hour <= 14:
                congestion_level = "medium"
                flow_rate = 0.6
            else:
                congestion_level = "low"
                flow_rate = 0.8

            predictions.append({
                "time": future_time.isoformat(),
                "congestion_level": congestion_level,
                "flow_rate": flow_rate,
                "confidence": 0.7
            })

        return {
            "predictions": predictions,
            "overall_confidence": 0.7,
            "method": "time_pattern_based"
        }

    def _predict_v2g_opportunities(self, horizon_minutes: int) -> List[Dict[str, Any]]:
        """Predict V2G trading opportunities"""
        opportunities = []
        current_time = datetime.now()

        # Peak hours typically have higher V2G value
        for i in range(0, horizon_minutes, 30):  # 30-minute intervals
            future_time = current_time + timedelta(minutes=i)
            hour = future_time.hour

            if 17 <= hour <= 20:  # Evening peak
                opportunity = {
                    "time": future_time.isoformat(),
                    "opportunity_level": "high",
                    "expected_rate": 1.2,
                    "confidence": 0.8,
                    "reason": "Evening peak demand period"
                }
            elif 7 <= hour <= 9:  # Morning peak
                opportunity = {
                    "time": future_time.isoformat(),
                    "opportunity_level": "medium",
                    "expected_rate": 0.9,
                    "confidence": 0.7,
                    "reason": "Morning peak demand period"
                }
            else:
                opportunity = {
                    "time": future_time.isoformat(),
                    "opportunity_level": "low",
                    "expected_rate": 0.3,
                    "confidence": 0.6,
                    "reason": "Off-peak period"
                }

            opportunities.append(opportunity)

        return opportunities

    def _predict_grid_stability(self, horizon_minutes: int) -> Dict[str, Any]:
        """Predict grid stability over time horizon"""
        # Simple stability prediction based on current state
        base_stability = 0.9  # Assume good baseline stability

        predictions = []
        current_time = datetime.now()

        for i in range(0, horizon_minutes, 20):  # 20-minute intervals
            future_time = current_time + timedelta(minutes=i)
            hour = future_time.hour

            # Stability typically decreases during peak hours
            if 17 <= hour <= 19:  # Evening peak
                stability_score = base_stability - 0.2
            elif 7 <= hour <= 9:  # Morning peak
                stability_score = base_stability - 0.1
            else:
                stability_score = base_stability

            predictions.append({
                "time": future_time.isoformat(),
                "stability_score": stability_score,
                "risk_level": "high" if stability_score < 0.7 else "medium" if stability_score < 0.8 else "low"
            })

        return {
            "predictions": predictions,
            "average_stability": sum(p["stability_score"] for p in predictions) / len(predictions),
            "confidence": 0.75
        }

    def _identify_optimization_windows(self, horizon_minutes: int) -> List[Dict[str, Any]]:
        """Identify windows of opportunity for system optimization"""
        windows = []
        current_time = datetime.now()

        # Look for periods of low demand and good stability
        for i in range(0, horizon_minutes, 60):  # Hourly windows
            future_time = current_time + timedelta(minutes=i)
            hour = future_time.hour

            # Off-peak hours are good for optimization
            if 23 <= hour or hour <= 5:
                windows.append({
                    "start_time": future_time.isoformat(),
                    "duration_minutes": 60,
                    "optimization_type": "maintenance",
                    "priority": "high",
                    "description": "Low demand period suitable for system maintenance"
                })
            elif 10 <= hour <= 16 and hour not in [12, 13]:  # Mid-day, avoid lunch
                windows.append({
                    "start_time": future_time.isoformat(),
                    "duration_minutes": 30,
                    "optimization_type": "rebalancing",
                    "priority": "medium",
                    "description": "Moderate demand period suitable for load rebalancing"
                })

        return windows


class ContextAnalyzer:
    """Advanced context analysis and understanding"""

    def __init__(self):
        self.context_history = deque(maxlen=100)
        self.intent_patterns = self._build_intent_patterns()
        self.context_weights = self._initialize_context_weights()

    def _build_intent_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Build comprehensive intent pattern recognition"""
        return {
            "emergency_response": {
                "keywords": ["emergency", "critical", "urgent", "failure", "blackout", "outage"],
                "priority": 10,
                "response_mode": "emergency",
                "requires_immediate_action": True
            },
            "technical_analysis": {
                "keywords": ["analyze", "technical", "detailed", "deep", "research", "study"],
                "priority": 8,
                "response_mode": "expert",
                "requires_detailed_data": True
            },
            "optimization_request": {
                "keywords": ["optimize", "improve", "efficiency", "better", "enhance"],
                "priority": 7,
                "response_mode": "advisor",
                "requires_recommendations": True
            },
            "status_inquiry": {
                "keywords": ["status", "state", "condition", "health", "operational"],
                "priority": 5,
                "response_mode": "assistant",
                "requires_current_data": True
            },
            "learning_request": {
                "keywords": ["explain", "how", "why", "what", "learn", "understand"],
                "priority": 4,
                "response_mode": "assistant",
                "requires_explanation": True
            }
        }

    def _initialize_context_weights(self) -> Dict[str, float]:
        """Initialize context weighting system"""
        return {
            "recency": 0.4,      # Recent messages have more weight
            "frequency": 0.3,     # Frequently mentioned topics have more weight
            "urgency": 0.2,      # Urgent topics get priority
            "user_expertise": 0.1 # User's technical level affects response
        }

    def analyze_conversation_context(self, message: str, user_context: Dict[str, Any], system_state: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze conversation context for intelligent response generation"""

        context_analysis = {
            "timestamp": datetime.now().isoformat(),
            "message_intent": self._analyze_message_intent(message),
            "context_continuity": self._analyze_context_continuity(message, user_context),
            "system_relevance": self._analyze_system_relevance(message, system_state),
            "urgency_level": self._calculate_urgency_level(message, system_state),
            "response_strategy": self._determine_response_strategy(message, user_context, system_state),
            "information_needs": self._identify_information_needs(message),
            "follow_up_potential": self._assess_follow_up_potential(message, user_context)
        }

        # Store for context continuity
        self.context_history.append({
            "message": message,
            "analysis": context_analysis,
            "timestamp": datetime.now()
        })

        return context_analysis

    def _analyze_message_intent(self, message: str) -> Dict[str, Any]:
        """Analyze message intent using advanced pattern matching"""
        message_lower = message.lower()
        detected_intents = []

        for intent_name, intent_config in self.intent_patterns.items():
            keyword_matches = sum(1 for keyword in intent_config["keywords"] if keyword in message_lower)
            if keyword_matches > 0:
                confidence = min(1.0, keyword_matches / len(intent_config["keywords"]) * 2)
                detected_intents.append({
                    "intent": intent_name,
                    "confidence": confidence,
                    "priority": intent_config["priority"],
                    "config": intent_config
                })

        # Sort by confidence * priority
        detected_intents.sort(key=lambda x: x["confidence"] * x["priority"], reverse=True)

        return {
            "primary_intent": detected_intents[0] if detected_intents else None,
            "all_intents": detected_intents,
            "complexity_score": len(detected_intents) + len(message.split()),
            "question_type": self._classify_question_type(message)
        }

    def _classify_question_type(self, message: str) -> str:
        """Classify the type of question being asked"""
        message_lower = message.lower()

        if any(word in message_lower for word in ["what", "which", "who"]):
            return "factual"
        elif any(word in message_lower for word in ["how", "why"]):
            return "explanatory"
        elif any(word in message_lower for word in ["should", "recommend", "suggest"]):
            return "advisory"
        elif any(word in message_lower for word in ["when", "where"]):
            return "situational"
        elif "?" in message:
            return "interrogative"
        else:
            return "statement"

    def _analyze_context_continuity(self, message: str, user_context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze how the message relates to conversation history"""
        recent_messages = list(self.context_history)[-5:]  # Last 5 exchanges

        if not recent_messages:
            return {"continuity_score": 0.0, "context_shift": True, "topic_consistency": 0.0}

        # Analyze topic continuity
        current_words = set(message.lower().split())
        recent_words = set()

        for hist_msg in recent_messages:
            recent_words.update(hist_msg["message"].lower().split())

        overlap = len(current_words.intersection(recent_words))
        continuity_score = overlap / len(current_words.union(recent_words)) if current_words.union(recent_words) else 0

        return {
            "continuity_score": continuity_score,
            "context_shift": continuity_score < 0.3,
            "topic_consistency": continuity_score,
            "conversation_depth": len(recent_messages)
        }

    def _analyze_system_relevance(self, message: str, system_state: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze how relevant the message is to current system state"""
        message_lower = message.lower()

        # Check relevance to system components
        relevance_scores = {}

        system_keywords = {
            "power_grid": ["power", "grid", "substation", "electricity", "load", "voltage"],
            "vehicles": ["vehicle", "car", "traffic", "sumo", "ev", "electric"],
            "v2g": ["v2g", "vehicle to grid", "energy trading", "discharge", "bidirectional"],
            "ml": ["ml", "machine learning", "prediction", "analytics", "ai"],
            "charging": ["charging", "station", "battery", "soc", "plug"]
        }

        for component, keywords in system_keywords.items():
            matches = sum(1 for keyword in keywords if keyword in message_lower)
            relevance_scores[component] = matches / len(keywords)

        # Check urgency based on system state
        system_issues = []
        stats = system_state.get("system_stats", {})

        if stats.get("substations_operational", 0) < stats.get("total_substations", 0):
            system_issues.append("substation_failures")

        ml_data = system_state.get("ml_data", {})
        if len(ml_data.get("anomalies", [])) > 0:
            system_issues.append("anomalies_detected")

        return {
            "component_relevance": relevance_scores,
            "most_relevant_component": max(relevance_scores.items(), key=lambda x: x[1])[0] if relevance_scores else None,
            "system_issues_relevance": [issue for issue in system_issues if any(keyword in message_lower for keyword in issue.split('_'))],
            "overall_relevance": max(relevance_scores.values()) if relevance_scores else 0.0
        }

    def _calculate_urgency_level(self, message: str, system_state: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate the urgency level of the request"""
        urgency_keywords = {
            "critical": 1.0,
            "emergency": 1.0,
            "urgent": 0.9,
            "immediate": 0.8,
            "asap": 0.8,
            "now": 0.7,
            "quickly": 0.6,
            "soon": 0.4
        }

        message_lower = message.lower()
        urgency_score = max([score for keyword, score in urgency_keywords.items() if keyword in message_lower] + [0.0])

        # Increase urgency based on system state
        system_urgency = 0.0
        stats = system_state.get("system_stats", {})

        if stats.get("substations_operational", 0) < stats.get("total_substations", 1) * 0.8:
            system_urgency = max(system_urgency, 0.7)

        ml_data = system_state.get("ml_data", {})
        high_severity_anomalies = [a for a in ml_data.get("anomalies", []) if a.get("severity") == "HIGH"]
        if high_severity_anomalies:
            system_urgency = max(system_urgency, 0.8)

        final_urgency = max(urgency_score, system_urgency)

        return {
            "urgency_score": final_urgency,
            "urgency_level": "critical" if final_urgency > 0.8 else "high" if final_urgency > 0.6 else "medium" if final_urgency > 0.3 else "low",
            "message_urgency": urgency_score,
            "system_urgency": system_urgency,
            "requires_immediate_response": final_urgency > 0.7
        }

    def _determine_response_strategy(self, message: str, user_context: Dict[str, Any], system_state: Dict[str, Any]) -> Dict[str, Any]:
        """Determine the optimal response strategy"""
        intent_analysis = self._analyze_message_intent(message)
        urgency = self._calculate_urgency_level(message, system_state)

        primary_intent = intent_analysis.get("primary_intent")

        if urgency["urgency_level"] == "critical":
            strategy = "emergency_response"
        elif primary_intent and primary_intent["config"].get("requires_detailed_data"):
            strategy = "detailed_analysis"
        elif intent_analysis["complexity_score"] > 20:
            strategy = "comprehensive_response"
        else:
            strategy = "standard_response"

        return {
            "strategy": strategy,
            "response_length": "long" if strategy in ["detailed_analysis", "comprehensive_response"] else "medium",
            "include_visualizations": intent_analysis["complexity_score"] > 15,
            "include_recommendations": primary_intent and primary_intent["config"].get("requires_recommendations", False),
            "use_technical_language": user_context.get("technical_level", 5) > 7,
            "priority_level": urgency["urgency_level"]
        }

    def _identify_information_needs(self, message: str) -> List[str]:
        """Identify what information is needed to answer the question"""
        needs = []
        message_lower = message.lower()

        if any(word in message_lower for word in ["status", "state", "condition"]):
            needs.append("current_system_status")

        if any(word in message_lower for word in ["predict", "forecast", "future", "will"]):
            needs.append("predictions")

        if any(word in message_lower for word in ["why", "cause", "reason"]):
            needs.append("causal_analysis")

        if any(word in message_lower for word in ["optimize", "improve", "better"]):
            needs.append("optimization_recommendations")

        if any(word in message_lower for word in ["compare", "versus", "vs"]):
            needs.append("comparative_analysis")

        if any(word in message_lower for word in ["historical", "past", "trend"]):
            needs.append("historical_data")

        return needs

    def _assess_follow_up_potential(self, message: str, user_context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess the potential for follow-up questions"""
        complexity = len(message.split())
        topic_breadth = len(set(message.lower().split()))

        follow_up_likelihood = min(1.0, (complexity + topic_breadth) / 50)

        return {
            "follow_up_likelihood": follow_up_likelihood,
            "likely_follow_up_topics": self._predict_follow_up_topics(message),
            "conversation_depth_potential": "high" if follow_up_likelihood > 0.7 else "medium" if follow_up_likelihood > 0.4 else "low"
        }

    def _predict_follow_up_topics(self, message: str) -> List[str]:
        """Predict likely follow-up topics"""
        topics = []
        message_lower = message.lower()

        if "status" in message_lower:
            topics.extend(["detailed_metrics", "historical_trends", "optimization_opportunities"])

        if any(word in message_lower for word in ["problem", "issue", "error"]):
            topics.extend(["root_cause_analysis", "solution_recommendations", "prevention_strategies"])

        if "optimize" in message_lower:
            topics.extend(["implementation_steps", "expected_results", "monitoring_approach"])

        return topics


class SystemMonitor:
    """Real-time system monitoring and intelligent alerting"""

    def __init__(self, integrated_system, ml_engine, v2g_manager):
        self.integrated_system = integrated_system
        self.ml_engine = ml_engine
        self.v2g_manager = v2g_manager

        self.monitoring_thread = None
        self.is_monitoring = False
        self.alert_thresholds = self._initialize_alert_thresholds()
        self.metric_history = defaultdict(deque)

        self._start_monitoring()

    def _initialize_alert_thresholds(self) -> Dict[str, Any]:
        """Initialize alert thresholds for various metrics"""
        return {
            "substation_failure_rate": 0.2,  # 20% failures trigger alert
            "grid_efficiency": 0.8,          # Below 80% efficiency
            "anomaly_score": 0.6,            # Anomaly score above 0.6
            "v2g_utilization": 0.3,          # Below 30% utilization during peak
            "prediction_accuracy": 0.7        # Below 70% accuracy
        }

    def _start_monitoring(self):
        """Start background monitoring thread"""
        self.is_monitoring = True
        self.monitoring_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitoring_thread.start()
        print("System Monitor started - real-time intelligent monitoring active")

    def _monitoring_loop(self):
        """Main monitoring loop"""
        while self.is_monitoring:
            try:
                self._collect_metrics()
                self._analyze_trends()
                self._check_alert_conditions()
                time.sleep(30)  # Monitor every 30 seconds
            except Exception as e:
                print(f"Monitoring error: {e}")
                time.sleep(60)  # Wait longer on error

    def _collect_metrics(self):
        """Collect current system metrics"""
        timestamp = datetime.now()

        # Power grid metrics
        substations = self.integrated_system.substations
        operational_substations = sum(1 for s in substations.values() if s.get("operational", False))
        total_substations = len(substations)

        grid_health = operational_substations / max(total_substations, 1)

        # ML metrics
        ml_metrics = {}
        if self.ml_engine:
            try:
                ml_data = self.ml_engine.get_ml_dashboard_data()
                ml_metrics = ml_data.get("metrics", {})
            except:
                pass

        # V2G metrics
        v2g_metrics = {}
        if self.v2g_manager:
            try:
                v2g_data = self.v2g_manager.get_v2g_dashboard_data()
                v2g_metrics = {
                    "active_sessions": v2g_data.get("active_sessions", 0),
                    "total_earnings": v2g_data.get("total_earnings", 0),
                    "utilization": v2g_data.get("utilization_rate", 0)
                }
            except:
                pass

        # Store metrics
        metrics = {
            "timestamp": timestamp,
            "grid_health": grid_health,
            "operational_substations": operational_substations,
            "total_substations": total_substations,
            "ml_metrics": ml_metrics,
            "v2g_metrics": v2g_metrics
        }

        # Store in history (keep last 100 readings)
        for key, value in metrics.items():
            if key != "timestamp":
                self.metric_history[key].append((timestamp, value))
                if len(self.metric_history[key]) > 100:
                    self.metric_history[key].popleft()

    def _analyze_trends(self):
        """Analyze trends in system metrics"""
        # This could be expanded with more sophisticated trend analysis
        pass

    def _check_alert_conditions(self):
        """Check for alert conditions"""
        # This could trigger alerts based on thresholds
        # For now, just log significant changes

        if hasattr(self, '_last_grid_health'):
            current_metrics = dict(self.metric_history)
            if 'grid_health' in current_metrics and current_metrics['grid_health']:
                current_health = current_metrics['grid_health'][-1][1]
                if abs(current_health - self._last_grid_health) > 0.1:
                    print(f"Stats Grid health change detected: {self._last_grid_health:.2f} -> {current_health:.2f}")
                self._last_grid_health = current_health
        else:
            if 'grid_health' in self.metric_history and self.metric_history['grid_health']:
                self._last_grid_health = self.metric_history['grid_health'][-1][1]

    def get_system_insights(self) -> Dict[str, Any]:
        """Get comprehensive system insights"""
        insights = {
            "timestamp": datetime.now().isoformat(),
            "monitoring_status": "active" if self.is_monitoring else "inactive",
            "metrics_collected": len(self.metric_history),
            "alert_status": "normal",  # Could be enhanced
            "system_health_trend": self._calculate_health_trend(),
            "performance_summary": self._generate_performance_summary()
        }

        return insights

    def _calculate_health_trend(self) -> Dict[str, Any]:
        """Calculate overall system health trend"""
        if 'grid_health' not in self.metric_history or len(self.metric_history['grid_health']) < 2:
            return {"trend": "stable", "confidence": 0.0}

        recent_values = [value for timestamp, value in list(self.metric_history['grid_health'])[-10:]]
        if len(recent_values) >= 2:
            trend_direction = "improving" if recent_values[-1] > recent_values[0] else "declining" if recent_values[-1] < recent_values[0] else "stable"
            confidence = abs(recent_values[-1] - recent_values[0]) * 10  # Simple confidence measure
        else:
            trend_direction = "stable"
            confidence = 0.0

        return {
            "trend": trend_direction,
            "confidence": min(1.0, confidence),
            "current_value": recent_values[-1] if recent_values else 0.0
        }

    def _generate_performance_summary(self) -> Dict[str, Any]:
        """Generate performance summary"""
        summary = {
            "overall_status": "operational",
            "key_metrics": {},
            "recommendations": []
        }

        # Add current metric values
        for metric_name, metric_history in self.metric_history.items():
            if metric_history and metric_name != "timestamp":
                latest_value = metric_history[-1][1]
                if isinstance(latest_value, (int, float)):
                    summary["key_metrics"][metric_name] = latest_value

        return summary

    def stop_monitoring(self):
        """Stop the monitoring thread"""
        self.is_monitoring = False
        if self.monitoring_thread:
            self.monitoring_thread.join(timeout=5)


class AlertManager:
    """Intelligent alert management system"""

    def __init__(self):
        self.active_alerts = []
        self.alert_history = deque(maxlen=1000)
        self.alert_rules = self._initialize_alert_rules()

    def _initialize_alert_rules(self) -> Dict[str, Any]:
        """Initialize alert rules and thresholds"""
        return {
            "critical_system_failure": {
                "condition": "grid_health < 0.5",
                "severity": "CRITICAL",
                "message": "Critical system failure detected",
                "actions": ["emergency_response", "notify_operators"]
            },
            "high_anomaly_activity": {
                "condition": "anomaly_count > 5",
                "severity": "HIGH",
                "message": "High anomaly activity detected",
                "actions": ["investigate_anomalies", "increase_monitoring"]
            }
        }

    def evaluate_alerts(self, system_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Evaluate current system state for alert conditions"""
        new_alerts = []

        # This would contain logic to evaluate alert rules
        # For now, return empty list

        return new_alerts


class LearningEngine:
    """Continuous learning and adaptation engine"""

    def __init__(self):
        self.interaction_history = deque(maxlen=10000)
        self.user_preferences = defaultdict(dict)
        self.response_effectiveness = defaultdict(list)

    def record_interaction(self, user_id: str, question: str, response: str, feedback: Optional[float] = None):
        """Record user interaction for learning"""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "question": question,
            "response": response,
            "feedback": feedback,
            "question_hash": hashlib.md5(question.encode()).hexdigest()[:8]
        }

        self.interaction_history.append(interaction)

        if feedback is not None:
            self.response_effectiveness[interaction["question_hash"]].append(feedback)

    def get_learning_insights(self) -> Dict[str, Any]:
        """Get insights from learning data"""
        return {
            "total_interactions": len(self.interaction_history),
            "average_feedback": self._calculate_average_feedback(),
            "common_topics": self._identify_common_topics(),
            "improvement_areas": self._identify_improvement_areas()
        }

    def _calculate_average_feedback(self) -> float:
        """Calculate average feedback score"""
        feedbacks = [interaction["feedback"] for interaction in self.interaction_history if interaction["feedback"] is not None]
        return statistics.mean(feedbacks) if feedbacks else 0.0

    def _identify_common_topics(self) -> List[str]:
        """Identify most commonly asked about topics"""
        topic_counts = defaultdict(int)

        for interaction in self.interaction_history:
            question = interaction["question"].lower()
            # Simple keyword extraction
            if "v2g" in question:
                topic_counts["v2g"] += 1
            if any(word in question for word in ["power", "grid", "substation"]):
                topic_counts["power_grid"] += 1
            if any(word in question for word in ["ml", "machine learning", "prediction"]):
                topic_counts["machine_learning"] += 1

        return sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    def _identify_improvement_areas(self) -> List[str]:
        """Identify areas where responses could be improved"""
        improvements = []

        # Analyze response effectiveness
        for question_hash, feedbacks in self.response_effectiveness.items():
            if feedbacks and statistics.mean(feedbacks) < 3.0:  # Below average feedback
                improvements.append(f"Improve responses for question type: {question_hash}")

        return improvements[:3]  # Top 3 improvement areas


class UserBehaviorAnalyzer:
    """Analyze user behavior patterns for personalization"""

    def __init__(self):
        self.user_sessions = defaultdict(list)
        self.user_preferences = defaultdict(dict)
        self.interaction_patterns = defaultdict(list)

    def analyze_user_behavior(self, user_id: str, interaction_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze user behavior patterns"""

        # Record interaction
        self.user_sessions[user_id].append({
            "timestamp": datetime.now().isoformat(),
            "interaction": interaction_data
        })

        # Analyze patterns
        behavior_analysis = {
            "session_count": len(self.user_sessions[user_id]),
            "preferred_topics": self._get_preferred_topics(user_id),
            "technical_level": self._estimate_technical_level(user_id),
            "interaction_style": self._analyze_interaction_style(user_id),
            "peak_usage_times": self._identify_peak_times(user_id)
        }

        return behavior_analysis

    def _get_preferred_topics(self, user_id: str) -> List[str]:
        """Get user's preferred topics based on interaction history"""
        sessions = self.user_sessions[user_id]
        topic_counts = defaultdict(int)

        for session in sessions:
            interaction = session.get("interaction", {})
            message = interaction.get("message", "").lower()

            # Simple topic detection
            if "v2g" in message:
                topic_counts["v2g"] += 1
            if any(word in message for word in ["power", "grid"]):
                topic_counts["power_grid"] += 1
            if "ml" in message or "machine learning" in message:
                topic_counts["machine_learning"] += 1

        return sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)

    def _estimate_technical_level(self, user_id: str) -> int:
        """Estimate user's technical expertise level (1-10)"""
        sessions = self.user_sessions[user_id]
        technical_keywords = ["algorithm", "neural", "optimization", "regression", "api", "protocol"]

        technical_usage = 0
        total_words = 0

        for session in sessions:
            interaction = session.get("interaction", {})
            message = interaction.get("message", "").lower()
            words = message.split()
            total_words += len(words)
            technical_usage += sum(1 for word in words if word in technical_keywords)

        if total_words == 0:
            return 5  # Default medium level

        technical_ratio = technical_usage / total_words
        return min(10, max(1, int(technical_ratio * 50 + 5)))  # Scale to 1-10

    def _analyze_interaction_style(self, user_id: str) -> str:
        """Analyze user's interaction style"""
        sessions = self.user_sessions[user_id]

        if len(sessions) < 3:
            return "new_user"

        # Analyze message characteristics
        avg_message_length = statistics.mean([
            len(session.get("interaction", {}).get("message", "").split())
            for session in sessions
        ])

        question_ratio = sum(1 for session in sessions
                           if "?" in session.get("interaction", {}).get("message", "")) / len(sessions)

        if avg_message_length > 20:
            return "detailed_inquirer"
        elif question_ratio > 0.7:
            return "frequent_questioner"
        elif avg_message_length < 5:
            return "brief_communicator"
        else:
            return "balanced_user"

    def _identify_peak_times(self, user_id: str) -> List[int]:
        """Identify user's peak usage hours"""
        sessions = self.user_sessions[user_id]
        hour_counts = defaultdict(int)

        for session in sessions:
            timestamp = datetime.fromisoformat(session["timestamp"].replace('Z', '+00:00'))
            hour = timestamp.hour
            hour_counts[hour] += 1

        # Return top 3 peak hours
        return sorted(hour_counts.items(), key=lambda x: x[1], reverse=True)[:3]


class PerformanceTracker:
    """Track AI performance and system metrics"""

    def __init__(self):
        self.response_times = deque(maxlen=1000)
        self.accuracy_scores = deque(maxlen=1000)
        self.user_satisfaction = deque(maxlen=1000)

    def record_response_time(self, duration: float):
        """Record response generation time"""
        self.response_times.append({
            "timestamp": datetime.now().isoformat(),
            "duration": duration
        })

    def record_accuracy_score(self, score: float):
        """Record accuracy score for a response"""
        self.accuracy_scores.append({
            "timestamp": datetime.now().isoformat(),
            "score": score
        })

    def record_user_satisfaction(self, rating: float):
        """Record user satisfaction rating"""
        self.user_satisfaction.append({
            "timestamp": datetime.now().isoformat(),
            "rating": rating
        })

    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics"""
        return {
            "avg_response_time": statistics.mean([r["duration"] for r in self.response_times]) if self.response_times else 0,
            "avg_accuracy": statistics.mean([a["score"] for a in self.accuracy_scores]) if self.accuracy_scores else 0,
            "avg_satisfaction": statistics.mean([s["rating"] for s in self.user_satisfaction]) if self.user_satisfaction else 0,
            "total_responses": len(self.response_times),
            "performance_trend": self._calculate_performance_trend()
        }

    def _calculate_performance_trend(self) -> str:
        """Calculate overall performance trend"""
        if len(self.response_times) < 10:
            return "insufficient_data"

        recent_times = [r["duration"] for r in list(self.response_times)[-10:]]
        earlier_times = [r["duration"] for r in list(self.response_times)[-20:-10]]

        if not earlier_times:
            return "stable"

        recent_avg = statistics.mean(recent_times)
        earlier_avg = statistics.mean(earlier_times)

        if recent_avg < earlier_avg * 0.9:
            return "improving"
        elif recent_avg > earlier_avg * 1.1:
            return "declining"
        else:
            return "stable"


class ConversationAnalytics:
    """Advanced conversation analytics and insights"""

    def __init__(self):
        self.conversation_metrics = {}
        self.topic_analysis = defaultdict(list)
        self.sentiment_tracking = deque(maxlen=1000)

    def analyze_conversation(self, conversation_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze conversation patterns and extract insights"""

        analysis = {
            "conversation_length": conversation_data.get("message_count", 0),
            "topic_diversity": self._calculate_topic_diversity(conversation_data),
            "complexity_score": self._calculate_complexity_score(conversation_data),
            "user_engagement": self._assess_user_engagement(conversation_data),
            "resolution_effectiveness": self._assess_resolution_effectiveness(conversation_data)
        }

        return analysis

    def _calculate_topic_diversity(self, conversation_data: Dict[str, Any]) -> float:
        """Calculate diversity of topics discussed"""
        # Simplified topic diversity calculation
        messages = conversation_data.get("messages", [])
        unique_topics = set()

        for message in messages:
            content = message.get("content", "").lower()
            if "v2g" in content:
                unique_topics.add("v2g")
            if any(word in content for word in ["power", "grid"]):
                unique_topics.add("power_grid")
            if "ml" in content:
                unique_topics.add("machine_learning")

        return len(unique_topics) / max(1, len(messages)) if messages else 0

    def _calculate_complexity_score(self, conversation_data: Dict[str, Any]) -> float:
        """Calculate conversation complexity score"""
        messages = conversation_data.get("messages", [])
        if not messages:
            return 0.0

        total_complexity = sum(len(msg.get("content", "").split()) for msg in messages)
        return total_complexity / len(messages)

    def _assess_user_engagement(self, conversation_data: Dict[str, Any]) -> Dict[str, Any]:
        """Assess user engagement level"""
        messages = conversation_data.get("messages", [])
        user_messages = [msg for msg in messages if msg.get("sender") == "user"]

        return {
            "message_ratio": len(user_messages) / max(1, len(messages)),
            "avg_message_length": statistics.mean([len(msg.get("content", "").split()) for msg in user_messages]) if user_messages else 0,
            "question_frequency": sum(1 for msg in user_messages if "?" in msg.get("content", "")) / max(1, len(user_messages))
        }

    def _assess_resolution_effectiveness(self, conversation_data: Dict[str, Any]) -> Dict[str, Any]:
        """Assess how effectively issues were resolved"""
        # This would require more sophisticated analysis of conversation outcomes
        # For now, return placeholder data
        return {
            "resolution_score": 0.8,  # Placeholder
            "follow_up_needed": False,
            "satisfaction_indicator": "positive"
        }


class BackgroundProcessor:
    """Handle background processing tasks"""

    def __init__(self):
        self.task_queue = deque()
        self.processing_thread = None
        self.is_processing = False

    def start_processing(self):
        """Start background processing thread"""
        self.is_processing = True
        self.processing_thread = threading.Thread(target=self._processing_loop, daemon=True)
        self.processing_thread.start()

    def _processing_loop(self):
        """Main processing loop"""
        while self.is_processing:
            try:
                if self.task_queue:
                    task = self.task_queue.popleft()
                    self._process_task(task)
                else:
                    time.sleep(1)  # Wait for tasks
            except Exception as e:
                print(f"Background processing error: {e}")
                time.sleep(5)

    def _process_task(self, task: Dict[str, Any]):
        """Process a background task"""
        task_type = task.get("type")

        if task_type == "analyze_patterns":
            # Perform pattern analysis
            pass
        elif task_type == "update_cache":
            # Update analysis cache
            pass
        elif task_type == "generate_insights":
            # Generate system insights
            pass

    def add_task(self, task: Dict[str, Any]):
        """Add a task to the processing queue"""
        self.task_queue.append(task)

    def stop_processing(self):
        """Stop background processing"""
        self.is_processing = False
        if self.processing_thread:
            self.processing_thread.join(timeout=5)