from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
db = SQLAlchemy(app)

# Models (Course, User, Category, etc.)
# class Course(db.Model):
class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=db.func.current_timestamp())

    # ----- CRUD Routes for Course -----

# Create a new course
@app.route('/api/courses', methods=['POST'])
def create_course():
    data = request.json
    course = Course(
        title=data['title'],
        description=data['description'],
        instructor=data['instructor'],
        duration=data['duration'],
        category=data['category'],
        price=data.get('price'),
        rating=data.get('rating')
    )
    db.session.add(course)
    db.session.commit()
    return jsonify({'message': 'Course created successfully!'}), 201


# Get all courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])


# Get a specific course by ID
@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'message': 'Course not found!'}), 404
    return jsonify(course.to_dict())


# Update a course
@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'message': 'Course not found!'}), 404

    data = request.json
    course.title = data['title']
    course.description = data['description']
    course.instructor = data['instructor']
    course.duration = data['duration']
    course.category = data['category']
    course.price = data.get('price')
    course.rating = data.get('rating')
    db.session.commit()

    return jsonify({'message': 'Course updated successfully!'})


# Delete a course
@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'message': 'Course not found!'}), 404
    db.session.delete(course)
    db.session.commit()
    return jsonify({'message': 'Course deleted successfully!'}), 200




if __name__ == '__main__':
    app.run(debug=True)

# ----- CRUD Routes for User, Category, and SavedCourse -----
# (Similar to the CRUD routes for Course, but with corresponding model classes)


# class User(db.Model):
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    # ----- CRUD Routes for User -----

# Create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'}), 201

# Get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Get a specific user by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    return jsonify(user.to_dict())

# Update a user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404

    data = request.json
    user.username = data['username']
    user.email = data['email']
    db.session.commit()

    return jsonify({'message': 'User updated successfully!'})

# Delete a user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)    


# class Category(db.Model):
class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(100), nullable=False)

    # ----- CRUD Routes for Category -----

# Create a new category
@app.route('/api/categories', methods=['POST'])
def create_category():
    data = request.json
    category = Category(category_name=data['category_name'])
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category created successfully!'}), 201

# Get all categories
@app.route('/api/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

# Get a specific category by ID
@app.route('/api/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found!'}), 404
    return jsonify(category.to_dict())

# Update a category
@app.route('/api/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found!'}), 404

    data = request.json
    category.category_name = data['category_name']
    db.session.commit()

    return jsonify({'message': 'Category updated successfully!'})

# Delete a category
@app.route('/api/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found!'}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)

# class Saved Courses(db.Model):
class SavedCourse(db.Model):
    saved_course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    saved_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    # ----- CRUD Routes for Saved Courses -----

# Create a new saved course
@app.route('/api/saved_courses', methods=['POST'])
def create_saved_course():
    data = request.json
    user_id = data['user_id']
    course_id = data['course_id']

    # Check if the user and course exist in the database
    user = User.query.get(user_id)
    course = Course.query.get(course_id)

    if not user or not course:
        return jsonify({'message': 'User or course not found!'}), 404

    saved_course = SavedCourse(user_id=user_id, course_id=course_id)
    db.session.add(saved_course)
    db.session.commit()

    return jsonify({'message': 'Course saved successfully!'}), 201

# Get all saved courses
@app.route('/api/saved_courses', methods=['GET'])
def get_saved_courses():
    saved_courses = SavedCourse.query.all()
    return jsonify([saved_course.to_dict() for saved_course in saved_courses])

# Get saved courses for a specific user
@app.route('/api/saved_courses/<int:user_id>', methods=['GET'])
def get_saved_courses_by_user(user_id):
    saved_courses = SavedCourse.query.filter_by(user_id=user_id).all()
    return jsonify([saved_course.to_dict() for saved_course in saved_courses])

# Delete a saved course
@app.route('/api/saved_courses/<int:saved_course_id>', methods=['DELETE'])
def delete_saved_course(saved_course_id):
    saved_course = SavedCourse.query.get(saved_course_id)
    if not saved_course:
        return jsonify({'message': 'Saved course not found!'}), 404
    db.session.delete(saved_course)
    db.session.commit()
    return jsonify({'message': 'Saved course deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
