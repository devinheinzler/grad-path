from flask import Blueprint, request, jsonify
from database import db
from models import User, Category, Course, SavedCourse

user_routes = Blueprint('user_routes', __name__)
category_routes = Blueprint('category_routes', __name__)
course_routes = Blueprint('course_routes', __name__)
saved_course_routes = Blueprint('saved_course_routes', __name__)

# Routes for the User model

@user_routes.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'}), 201

@user_routes.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_routes.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    return jsonify(user.to_dict())

@user_routes.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404

    data = request.json
    user.username = data['username']
    user.email = data['email']
    db.session.commit()

    return jsonify({'message': 'User updated successfully!'})

@user_routes.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'}), 200

# Routes for the Category model

# Create a new category
@category_routes.route('/api/categories', methods=['POST'])
def create_category():
    data = request.json
    category_name = data['category_name']
    category = Category(category_name=category_name)
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category created successfully!'}), 201

# Get all categories
@category_routes.route('/api/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

# Get a specific category by ID
@category_routes.route('/api/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found!'}), 404
    return jsonify(category.to_dict())

# Update a category
@category_routes.route('/api/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found!'}), 404

    data = request.json
    category.category_name = data['category_name']
    db.session.commit()

    return jsonify({'message': 'Category updated successfully!'})

# Delete a category
@category_routes.route('/api/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found!'}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully!'}), 200

# Routes for the Course model

# Create a new course
@course_routes.route('/api/courses', methods=['POST'])
def create_course():
    data = request.json
    title = data['title']
    description = data['description']
    instructor = data['instructor']
    duration = data['duration']
    category_id = data['category_id']
    price = data['price']
    rating = data['rating']

    course = Course(title=title, description=description, instructor=instructor,
                    duration=duration, category_id=category_id, price=price, rating=rating)

    db.session.add(course)
    db.session.commit()
    return jsonify({'message': 'Course created successfully!'}), 201

# Get all courses
@course_routes.route('/api/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])

# Get a specific course by ID
@course_routes.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'message': 'Course not found!'}), 404
    return jsonify(course.to_dict())

# Update a course
@course_routes.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'message': 'Course not found!'}), 404

    data = request.json
    course.title = data['title']
    course.description = data['description']
    course.instructor = data['instructor']
    course.duration = data['duration']
    course.category_id = data['category_id']
    course.price = data['price']
    course.rating = data['rating']

    db.session.commit()

    return jsonify({'message': 'Course updated successfully!'})

# Delete a course
@course_routes.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'message': 'Course not found!'}), 404
    db.session.delete(course)
    db.session.commit()
    return jsonify({'message': 'Course deleted successfully!'}), 200

# Routes for the SavedCourse model

# Create a new saved course
@saved_course_routes.route('/api/saved_courses', methods=['POST'])
def create_saved_course():
    data = request.json
    user_id = data['user_id']
    course_id = data['course_id']

    saved_course = SavedCourse(user_id=user_id, course_id=course_id)
    db.session.add(saved_course)
    db.session.commit()
    return jsonify({'message': 'Course saved successfully!'}), 201

# Get all saved courses for a specific user
@saved_course_routes.route('/api/saved_courses/<int:user_id>', methods=['GET'])
def get_saved_courses(user_id):
    saved_courses = SavedCourse.query.filter_by(user_id=user_id).all()
    return jsonify([saved_course.to_dict() for saved_course in saved_courses])

# Update a saved course (Not necessary in most cases, as saved courses are usually created and deleted)
@saved_course_routes.route('/api/saved_courses/<int:saved_course_id>', methods=['PUT'])
def update_saved_course(saved_course_id):
    saved_course = SavedCourse.query.get(saved_course_id)
    if not saved_course:
        return jsonify({'message': 'Saved course not found!'}), 404

    data = request.json
    saved_course.user_id = data['user_id']
    saved_course.course_id = data['course_id']
    db.session.commit()

    return jsonify({'message': 'Saved course updated successfully!'})

# Delete a saved course
@saved_course_routes.route('/api/saved_courses/<int:saved_course_id>', methods=['DELETE'])
def delete_saved_course(saved_course_id):
    saved_course = SavedCourse.query.get(saved_course_id)
    if not saved_course:
        return jsonify({'message': 'Saved course not found!'}), 404
    db.session.delete(saved_course)
    db.session.commit()
    return jsonify({'message': 'Saved course deleted successfully!'}), 200

