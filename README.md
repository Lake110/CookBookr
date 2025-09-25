# CookBookr 🍳

A social media-style recipe sharing website built with Django where users can create, share, and discover recipes while planning their weekly meals and generating shopping lists.

## Table of Contents

- [Project Overview](#project-overview)
- [User Stories & Acceptance Criteria (MVP)](#user-stories--acceptance-criteria-mvp)
- [Planned Models & Database Design](#planned-models--database-design)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Development Status](#development-status)
- [Testing](#testing)
- [Contributing](#contributing)

## Project Overview

**CookBookr** aims to create a vibrant online community for food enthusiasts to share their culinary creations, discover new recipes, and streamline their meal planning process.

### MVP Goals (Recipe Sharing)
- User registration and authentication system
- Create, read, update, and delete recipes
- Comment system for community interaction
- User profiles for recipe management

### Planned Iterations
- **Iteration 2**: Meal Planning - Weekly calendar-style meal planning with external recipe API integration
- **Iteration 3**: Shopping & Nutrition - Automated shopping list generation and nutrition tracking

## User Stories & Acceptance Criteria (MVP)

### 1. Register and Log In
**As a site user, I can register and log in so that I can share my own recipes.**

**Acceptance Criteria:**
- **AC1:** Given valid registration details, when I submit the form, then my account is created, and I am logged in.
- **AC2:** Given an existing account, when I submit correct login credentials, then I am logged in and redirected to the homepage.
- **AC3:** Given incorrect login details, when I attempt to log in, then I see an error message and remain on the login page.

### 2. Create a Recipe
**As a site user, I can create a recipe so that I can share it with others.**

**Acceptance Criteria:**
- **AC1:** Given I am logged in, when I submit a recipe with a title, ingredients, instructions, and optional photo, then the recipe is saved and appears in my list.
- **AC2:** Given required fields are left blank, when I attempt to submit, then I see a validation error.

### 3. View Recipes
**As a site user, I can view recipes so that I can try cooking them.**

**Acceptance Criteria:**
- **AC1:** Given multiple recipes exist, when I open the recipes page, then I see a list of recipes with title and summary.
- **AC2:** Given I click a recipe, when the detail page loads, then I see the full recipe including ingredients, instructions, and comments.

### 4. Comment on Recipes
**As a site user, I can comment on recipes so that I can give feedback or ask questions.**

**Acceptance Criteria:**
- **AC1:** Given I am logged in, when I submit a comment, then my comment appears under the recipe with my username and timestamp.
- **AC2:** Given I am not logged in, when I attempt to comment, then I am prompted to log in or register.

### 5. Edit/Delete My Recipes
**As a site user, I can edit or delete my own recipes so that I can keep them up to date.**

**Acceptance Criteria:**
- **AC1:** Given I am logged in and viewing my recipe, when I click "Edit" and update fields, then the recipe updates successfully.
- **AC2:** Given I am logged in and viewing my recipe, when I click "Delete," then the recipe is removed from the database.

### 6. Edit/Delete My Comments
**As a site user, I can edit or delete my own comments so that I can control what I post.**

**Acceptance Criteria:**
- **AC1:** Given I am logged in and viewing my comment, when I click "Edit" and update the text, then the updated comment is displayed.
- **AC2:** Given I am logged in and viewing my comment, when I click "Delete," then the comment is removed from the recipe page.

## Planned Models & Database Design

### Core Models (MVP)
- **User**: Django's built-in User model with custom profile extension
- **Recipe**: Main recipe model with title, description, ingredients, instructions, cooking time, servings
- **Comment**: User comments on recipes with timestamp and content
- **Category**: Recipe categories (cuisine types, dietary preferences)

### Model Relationships
- User → Recipe (One-to-Many: One user can create many recipes)
- User → Comment (One-to-Many: One user can make many comments)  
- Recipe → Comment (One-to-Many: One recipe can have many comments)
- Recipe → Category (Many-to-Many: Recipes can belong to multiple categories)

### Future Models (Later Iterations)
- **MealPlan**: Weekly meal planning structure
- **ShoppingList**: Generated shopping lists from meal plans
- **MealPlanItem**: Junction table for meal plan recipes
- **Nutrition**: Nutritional information for recipes

### Entity Relationship Diagrams

#### MVP Database Schema (Core Features)
![MVP ERD](<docs/Readme/images/Screenshot 2025-09-24 at 15.34.05 copy.png>)
*Shows the essential models needed for recipe sharing: User, Recipe, and Comment relationships.*

#### MVP + Iteration 2 (Meal Plan)
![ERD for meal plan incorperations](<docs/Readme/images/Screenshot 2025-09-25 at 14.23.04.png>)
*Shows interactions between MVP and Meal Plan Function.*

#### Complete Database Schema (All Iterations)
![all Iterations ERD Basic](<docs/Readme/images/Overall Project ERD copy.png>)
*Shows the full database design including meal planning, shopping lists, and all planned features.*


## Wireframes

Visual design wireframes for CookBookr across devices:

- **Phone Design**
  ![Phone Wireframe](<docs/Readme/images/Phone Design.jpg>)
- **Tablet Design**
  ![Tablet Wireframe](<docs/Readme/images/Tablet Design.jpg>)
- **PC Design**
  ![PC Wireframe](<docs/Readme/images/PC design.jpg>)

*These wireframes illustrate the planned user interface for mobile, tablet, and desktop experiences.*

## Tech Stack

### Backend
- **Python 3.8+**
- **Django 4.2+** - Web framework
- **PostgreSQL** - Production database (SQLite for development)
- **Django REST Framework** - API development (for future mobile app)

### Frontend
- **HTML5/CSS3**
- **JavaScript (ES6+)**
- **Bootstrap 5** - CSS framework for responsive design
- **Django Templates** - Server-side rendering

### Development Tools
- **Git/GitHub** - Version control
- **VS Code** - IDE
- **Django Debug Toolbar** - Development debugging
- **Pillow** - Image processing for recipe photos

### Deployment (Future)
- **Heroku** or **DigitalOcean** - Hosting
- **Cloudinary** - Image storage
- **WhiteNoise** - Static file serving

## Installation

*This project will run in Django. Detailed setup steps will be added as development progresses.*

### Quick Start (Development)
```bash
# Clone repository (once created)
git clone https://github.com/yourusername/cookbookr.git
cd cookbookr

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (requirements.txt to be created)
pip install django

# Run development server
python manage.py runserver
```

## Development Status

🚧 **This project is in early development phase**

- [ ] Project setup and initial Django configuration
- [ ] User authentication system
- [ ] Recipe model and CRUD operations
- [ ] Comment system
- [ ] Basic UI/UX implementation
- [ ] Testing implementation
- [ ] Deployment setup

## Testing

Tests will be added as features are implemented using Django's built-in testing framework.

## Contributing

This is currently a solo capstone project. Contribution guidelines will be added if the project becomes collaborative.

---

*This README is a living document and will be updated throughout the development process.*