from flask import Blueprint, request, jsonify

device_bp = Blueprint("device", __name__)

@device_bp.route("/api/register_device.html", methods=["POST"])
def register_device():
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "No data"}), 400

    return jsonify({"success": True, "message": "Device registered"})