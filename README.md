# Django REST Framework Practice Project

A comprehensive Django REST Framework (DRF) practice project focused on learning and implementing:

- APIViews
- GenericAPIView
- ViewSets
- ModelViewSet
- Mixins
- Pagination
- ORM Queries
- Aggregations
- Subqueries
- Filtering
- Serializer Validation
- REST API Design

This repository contains multiple practice apps built while learning Django ORM and DRF concepts. :contentReference[oaicite:0]{index=0}

---

# 🚀 Features

- Restaurant CRUD APIs
- Ratings Management APIs
- Sales APIs
- DRF ViewSets
- DRF Mixins
- GenericAPIView usage
- Pagination support
- ORM aggregation queries
- Filtering support
- Custom validation logic
- Subquery annotations
- Top-rated restaurant APIs
- Income analytics APIs

---

# 🧠 Concepts Covered

## Django REST Framework

- APIView
- GenericAPIView
- ModelViewSet
- Mixins
- Serializers
- Pagination
- Response handling
- Status codes
- Validation

---

## Django ORM

- `Avg()`
- `Count()`
- `Sum()`
- `Subquery()`
- `OuterRef()`
- `annotate()`
- `filter()`
- Query optimization

---

# 📂 Project Structure

```bash
project/
│
├── drf/
├── orm_drf/
├── restaurant/
├── testApp/
├── user/
├── manage.py
├── db.sqlite3
└── django_orm_practice.pdf
```

---

# 🍴 Restaurant Module

The main module demonstrates real-world REST API implementation for restaurant management.

### Features

- Restaurant CRUD operations
- Restaurant ratings
- Restaurant sales
- Top 5 restaurants by rating
- Highest income restaurants
- Pagination support
- Filtering support

---

# 🏗️ APIs Implemented

## Restaurant APIs

| Endpoint | Description |
|---|---|
| GET `/restaurants/` | Get all restaurants |
| GET `/restaurants/<id>/` | Get restaurant by ID |
| POST `/restaurants/` | Create restaurant |
| PUT `/restaurants/<id>/` | Update restaurant |
| DELETE `/restaurants/<id>/` | Delete restaurant |

---

## Rating APIs

| Endpoint | Description |
|---|---|
| GET `/ratings/` | Get ratings |
| POST `/ratings/` | Add rating |
| PUT `/ratings/<id>/` | Update rating |
| DELETE `/ratings/<id>/` | Delete rating |

---

## Sales APIs

| Endpoint | Description |
|---|---|
| GET `/sales/` | Get sales |
| POST `/sales/` | Add sales |
| PUT `/sales/<id>/` | Update sales |
| DELETE `/sales/<id>/` | Delete sales |

---

# 📊 Advanced ORM Queries

This project demonstrates advanced ORM usage like:

## Average Restaurant Rating

```python
Restaurant.objects.annotate(
    avg_rating=Avg('ratings__rating')
)
```

---

## Total Restaurant Income

```python
Restaurant.objects.annotate(
    total_sales=Sum('sales__income')
)
```

---

## Subquery Annotation

```python
avg_rating = Rating.objects.filter(
    pk=OuterRef('pk')
).annotate(
    avg_rating=Avg('rating')
).values('avg_rating')
```

---

# 🔥 DRF Features Demonstrated

## APIView Example

```python
class RestaurantAPIView(APIView):
    pass
```

---

## GenericAPIView + Mixins

```python
class RatingGenericAPIView(
    GenericAPIView,
    ListModelMixin,
    RetrieveModelMixin
):
    pass
```

---

## ModelViewSet

```python
class RestaurantModelViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
```

---

# 📄 Example Restaurant Payload

```json
{
    "name": "ATestRest1",
    "website": "http://test-rest.com/",
    "open_time": "12:20:05",
    "date_opened": "2020-07-30",
    "latitude": -36.6052075,
    "longitude": -97.945041,
    "restaurant_type": "IN"
}
```

---

# 🛠️ Installation

Clone the repository:

```bash
git clone <your-repo-url>
```

Move into the project directory:

```bash
cd <project-folder>
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install django djangorestframework
```

---

# ▶️ Run the Project

Apply migrations:

```bash
python manage.py migrate
```

Run development server:

```bash
python manage.py runserver
```

---

# 🌐 API Testing

You can test APIs using:

- Postman
- Thunder Client
- Insomnia
- DRF Browsable API

---

# 📚 Learning Goals

This project was built for practicing:

- Django ORM
- REST API development
- DRF architecture
- Query optimization
- Serializer validation
- API pagination
- Aggregation queries
- Production-style backend structure

---

# 🎯 Skills Demonstrated

- Backend API Development
- Django REST Framework
- ORM Query Optimization
- RESTful API Design
- Pagination & Filtering
- CRUD Operations
- Data Aggregation
- Serializer Validation

---

# 🔮 Future Improvements

Possible enhancements:

- JWT Authentication
- Permissions & Roles
- Swagger Documentation
- Docker Support
- PostgreSQL Integration
- Unit Testing
- Caching
- Async APIs
- Celery Integration

---

# 🙌 Acknowledgements

Built while learning and practicing:

- Django
- Django REST Framework
- Django ORM
- Backend API Architecture
