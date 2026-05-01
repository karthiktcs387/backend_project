from flask import Blueprint, request, jsonify
from models import db, Opportunity

opp_bp = Blueprint('opp', __name__)

# ✅ ADD OPPORTUNITY
@opp_bp.route('/add', methods=['POST'])
def add_opportunity():
    data = request.json

    # Validation
    required_fields = ['name', 'duration', 'start_date', 'description', 'skills', 'category', 'future_opportunities', 'admin_id']

    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field} is required"}), 400

    new_opp = Opportunity(
        name=data['name'],
        duration=data['duration'],
        start_date=data['start_date'],
        description=data['description'],
        skills=data['skills'],
        category=data['category'],
        future_opportunities=data['future_opportunities'],
        max_applicants=data.get('max_applicants'),
        admin_id=data['admin_id']
    )

    db.session.add(new_opp)
    db.session.commit()

    return jsonify({"message": "Opportunity added successfully"})


# ✅ VIEW ALL OPPORTUNITIES (only logged-in admin)
@opp_bp.route('/all/<int:admin_id>', methods=['GET'])
def get_opportunities(admin_id):
    opps = Opportunity.query.filter_by(admin_id=admin_id).all()
    if not opps:
        return jsonify({"message": "No opportunities found"})

    result = []
    for o in opps:
        result.append({
            "id": o.id,
            "name": o.name,
            "category": o.category,
            "duration": o.duration,
            "start_date": o.start_date,
            "description": o.description
        })

    return jsonify(result)


# ✅ VIEW DETAILS
@opp_bp.route('/detail/<int:id>', methods=['GET'])
def get_one(id):
    o = Opportunity.query.get(id)

    if not o:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "name": o.name,
        "duration": o.duration,
        "start_date": o.start_date,
        "description": o.description,
        "skills": o.skills,
        "category": o.category,
        "future_opportunities": o.future_opportunities,
        "max_applicants": o.max_applicants
    })


# ✅ UPDATE
@opp_bp.route('/update/<int:id>', methods=['PUT'])
def update_opportunity(id):
    data = request.json
    admin_id = data.get('admin_id')

    opp = Opportunity.query.filter_by(id=id, admin_id=admin_id).first()

    if not opp:
        return jsonify({"error": "Not allowed"}), 403

    opp.name = data['name']
    opp.duration = data['duration']
    opp.start_date = data['start_date']
    opp.description = data['description']
    opp.skills = data['skills']
    opp.category = data['category']
    opp.future_opportunities = data['future_opportunities']
    opp.max_applicants = data.get('max_applicants')

    db.session.commit()

    return jsonify({"message": "Updated successfully"})


# ✅ DELETE
@opp_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_opportunity(id):
    data = request.json
    admin_id = data.get('admin_id')

    opp = Opportunity.query.filter_by(id=id, admin_id=admin_id).first()

    if not opp:
        return jsonify({"error": "Not allowed"}), 403

    db.session.delete(opp)
    db.session.commit()

    return jsonify({"message": "Deleted successfully"})