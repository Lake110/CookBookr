# CookBookr

A social media-style recipe sharing website built with Django where users can create, share, and discover recipes while engaging with a vibrant culinary community through comments and interactions.

## Table of Contents

- [UX Design](#ux-design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
- [User Stories and Kanban Board](#user-stories-and-kanban-board)
- [Wireframes](#wireframes)
- [ERD Diagram](#erd-diagram)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
- [How AI Was Used](#how-ai-was-used)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
  - [Code Validation](#code-validation)
  - [LightHouse Testing](#lighthouse-testing)
- [Deployment](#deployment)
- [Credits and Acknowledgements](#credits-and-acknowledgements)
  - [Content](#content)
  - [Media](#media)

---

## UX Design

CookBookr was designed with a warm, inviting aesthetic that evokes the comfort and joy of home cooking while maintaining modern web standards and accessibility.

### Colour Scheme

The color palette was carefully chosen to create a warm, friendly atmosphere that encourages users to share their culinary creations:

#### Primary Colors
- **Cerulean (#437390)**: Used for accent colors, links, and hover states
- **Dark Cyan (#295657)**: Primary color for headers, buttons, and main UI elements
- **Burnt Sienna (#AA6056)**: Call-to-action buttons and important highlights

#### Supporting Colors
- **Eggplant (#754B6E)**: Background sections and cards
- **Brass (#C39D4D)**: Icons, borders, and subtle accents
- **Olive (#D7C974)**: Secondary sections and soft backgrounds
- **Cream (#FAF3E0)**: Main background for a warm, welcoming feel
- **Charcoal (#1C1C1C)**: Primary text for excellent readability

#### Color Psychology
The warm earth tones and muted colors were selected to:
- Create a cozy, kitchen-like atmosphere
- Ensure food photography looks appetizing against the backgrounds
- Maintain accessibility with proper contrast ratios
- Evoke feelings of comfort and home cooking

### Typography

Typography choices emphasize readability and warmth:

- **Primary Font**: System fonts for optimal performance and familiarity
- **Headings**: Bold weights to create clear hierarchy
- **Body Text**: Regular weight with optimal line spacing for recipe reading
- **Recipe Instructions**: Clear, numbered lists with adequate spacing
- **Meta Information**: Smaller, muted text for cooking times and servings

### Imagery

- **Recipe Cards**: Consistent square format for visual harmony
- **Placeholder Images**: Subtle gradients when user photos aren't available
- **Food Photography**: High contrast backgrounds to make food images pop
- **Icons**: FontAwesome icons for consistent, recognizable UI elements
- **Hero Section**: Warm gradient backgrounds using the brand color palette

---

## User Stories and Kanban Board

### Epic: User Authentication & Account Management

#### User Story 1: Register and Log In
**As a site user, I can register and log in so that I can share my own recipes.**

**Acceptance Criteria:**
- **AC1:** Given valid registration details, when I submit the form, then my account is created, and I am logged in.
- **AC2:** Given an existing account, when I submit correct login credentials, then I am logged in and redirected to the homepage.
- **AC3:** Given incorrect login details, when I attempt to log in, then I see an error message and remain on the login page.

**Status:** ✅ **Completed**

### Epic: Recipe Management

#### User Story 2: Create a Recipe
**As a site user, I can create a recipe so that I can share it with others.**

**Acceptance Criteria:**
- **AC1:** Given I am logged in, when I submit a recipe with a title, ingredients, instructions, and optional photo, then the recipe is saved and appears in my list.
- **AC2:** Given required fields are left blank, when I attempt to submit, then I see a validation error.

**Status:** ✅ **Completed**

#### User Story 3: View Recipes  
**As a site user, I can view recipes so that I can try cooking them.**

**Acceptance Criteria:**
- **AC1:** Given multiple recipes exist, when I open the recipes page, then I see a list of recipes with title and summary.
- **AC2:** Given I click a recipe, when the detail page loads, then I see the full recipe including ingredients, instructions, and comments.

**Status:** ✅ **Completed**

#### User Story 4: Edit/Delete My Recipes
**As a site user, I can edit or delete my own recipes so that I can keep them up to date.**

**Acceptance Criteria:**
- **AC1:** Given I am logged in and viewing my recipe, when I click "Edit" and update fields, then the recipe updates successfully.
- **AC2:** Given I am logged in and viewing my recipe, when I click "Delete," then the recipe is removed from the database.

**Status:** ✅ **Completed**

### Epic: Community Interaction

#### User Story 5: Comment on Recipes
**As a site user, I can comment on recipes so that I can give feedback or ask questions.**

**Acceptance Criteria:**
- **AC1:** Given I am logged in, when I submit a comment, then my comment appears under the recipe with my username and timestamp.
- **AC2:** Given I am not logged in, when I attempt to comment, then I am prompted to log in or register.

**Status:** ✅ **Completed**

#### User Story 6: Edit/Delete My Comments
**As a site user, I can edit or delete my own comments so that I can control what I post.**

**Acceptance Criteria:**
- **AC1:** Given I am logged in and viewing my comment, when I click "Edit" and update the text, then the updated comment is displayed.
- **AC2:** Given I am logged in and viewing my comment, when I click "Delete," then the comment is removed from the recipe page.

**Status:** ✅ **Completed**

### Kanban Board Progress
- **To Do**: Future meal planning features
- **In Progress**: UI/UX refinements
- **Done**: All MVP user stories completed
- **Testing**: Manual testing of all completed features

---

## Wireframes

Visual design wireframes for CookBookr across devices:

### Mobile Design (320px - 768px)
![Phone Wireframe](<docs/Readme/images/Phone Design.jpg>)
*Mobile-first approach with touch-friendly buttons and simplified navigation*

### Tablet Design (768px - 1024px)  
![Tablet Wireframe](<docs/Readme/images/Tablet Design.jpg>)
*Optimized for tablet viewing with improved layout spacing*

### Desktop Design (1024px+)
![PC Wireframe](<docs/Readme/images/PC design.jpg>)
*Full desktop experience with expanded navigation and content areas*

**Design Decisions:**
- **Mobile-first approach** ensures optimal experience on all devices
- **Card-based layout** for easy recipe browsing
- **Consistent navigation** across all screen sizes
- **Touch-friendly buttons** with adequate spacing
- **Responsive typography** that scales appropriately

---

## ERD Diagram

### Database Schema Design

#### MVP Database Schema (Current Implementation)
![MVP ERD](<docs/Readme/images/Screenshot 2025-09-24 at 15.34.05 copy.png>)
*Shows the essential models for recipe sharing: User, Recipe, and Comment relationships*

**Current Models:**
- **User**: Django's built-in User model
- **Recipe**: Core recipe model with all recipe data
- **Comment**: User comments with moderation system

#### Future Iterations Schema
![Complete ERD](<docs/Readme/images/Overall Project ERD copy.png>)
*Shows planned database expansion for meal planning and shopping features*

**Model Relationships:**
- User → Recipe (One-to-Many)
- User → Comment (One-to-Many)  
- Recipe → Comment (One-to-Many)
- Future: MealPlan → Recipe (Many-to-Many)

---

## Features

### Existing Features

#### 🏠 **Homepage & Navigation**
- **Responsive navigation bar** with user authentication status
- **Hero section** with warm gradient background
- **Recipe grid display** with pagination
- **Search functionality** for finding recipes
- **Mobile-optimized hamburger menu**

#### 👤 **User Authentication**
- **User registration** with form validation
- **Login/logout functionality** with session management
- **Password authentication** with Django's built-in security
- **User profile management**
- **Authentication-based navigation** (different menus for logged-in users)

#### 📝 **Recipe Management**
- **Create recipes** with rich form interface
- **Edit own recipes** with pre-populated forms
- **Delete recipes** with confirmation modals
- **Recipe detail views** with formatted ingredients and instructions
- **Author attribution** and timestamp tracking
- **Cooking time and servings display**

#### 💬 **Comment System**
- **Add comments** to recipes (authenticated users only)
- **Edit own comments** with inline editing
- **Delete comments** with confirmation
- **Comment moderation** system for new comments
- **Real-time comment updates** without page refresh
- **Author-only edit/delete permissions**

#### 🎨 **UI/UX Features**
- **Responsive design** that works on all devices
- **Warm color scheme** optimized for food content
- **Bootstrap 5 components** for consistent styling
- **Toast notifications** for user feedback
- **Loading states** for better user experience
- **Form validation** with helpful error messages
- **Accessibility features** (proper contrast, focus states)

#### 🔐 **Security Features**
- **CSRF protection** on all forms
- **User permission checks** for edit/delete operations
- **Comment moderation** to prevent spam
- **SQL injection protection** via Django ORM
- **XSS protection** with Django's built-in templating

### Features Left to Implement

#### 🗓️ **Meal Planning (Iteration 2)**
- Weekly calendar interface for meal planning
- Drag-and-drop recipe scheduling
- External recipe API integration
- Meal plan sharing with family/friends

#### 🛒 **Shopping Lists (Iteration 3)**
- Automatic shopping list generation from meal plans
- Ingredient quantity calculations
- Shopping list sharing and collaboration
- Store integration for online ordering

#### 📊 **Advanced Features**
- Recipe rating and review system
- Nutritional information display
- Recipe categories and advanced filtering
- Social features (following users, recipe collections)
- Recipe photo upload and management
- Advanced search with filters (prep time, dietary restrictions)

#### 📱 **Technical Enhancements**
- Progressive Web App (PWA) capabilities
- Recipe import from URLs
- Print-friendly recipe layouts
- Recipe scaling (adjust servings)
- Unit conversion tools
- Voice-activated cooking mode

#### 📚 **Learning Enhancement**
- **Django Best Practices**: AI explanations helped reinforce Django patterns
- **CSS Architecture**: Learned modern CSS organization techniques
- **JavaScript Patterns**: Improved understanding of modern JavaScript approaches
- **Testing Strategies**: Enhanced knowledge of Django testing methodologies

---

## Technologies Used

### Backend Technologies
- **Python 3.12** - Core programming language
- **Django 4.2+** - Web framework for rapid development
- **PostgreSQL** - Production database for data persistence
- **SQLite** - Development database for local testing
- **Django ORM** - Database abstraction layer
- **Django Authentication** - Built-in user management system

### Frontend Technologies  
- **HTML5** - Semantic markup for structure
- **CSS3** - Styling with modern features (Grid, Flexbox, Custom Properties)
- **JavaScript ES6+** - Interactive functionality
- **Bootstrap 5** - CSS framework for responsive design
- **FontAwesome** - Icon library for UI elements

### Development Tools
- **Git/GitHub** - Version control and code repository
- **VS Code** - Primary development environment
- **Django Debug Toolbar** - Development debugging and profiling
- **Chrome DevTools** - Frontend debugging and testing
- **Pillow** - Python image processing library

### Testing & Quality Assurance
- **Django Testing Framework** - Unit and integration testing
- **Manual Testing** - User experience validation
- **HTML/CSS Validators** - Code quality assurance
- **Lighthouse** - Performance and accessibility auditing

### Deployment & Production
- **Heroku** - Cloud platform for deployment (planned)
- **WhiteNoise** - Static file serving in production
- **Cloudinary** - Image storage and optimization (planned)
- **Environment Variables** - Secure configuration management

---

## How AI Was Used

AI tools were strategically integrated throughout the development process to enhance productivity and code quality:

### 🧠 **GitHub Copilot**
- **Code Completion**: Accelerated development with intelligent code suggestions
- **Function Generation**: Generated boilerplate code for Django views and models
- **CSS Styling**: Assisted with responsive design patterns and CSS optimization
- **JavaScript Logic**: Helped implement complex comment editing functionality
- **Documentation**: Generated code comments and docstrings

### 💡 **AI-Assisted Problem Solving**
- **Debugging Support**: Identified and resolved complex CSS and JavaScript issues
- **Database Design**: Validated model relationships and field choices
- **User Experience**: Suggested improvements for form handling and user feedback
- **Performance Optimization**: Recommended best practices for Django optimization

### 🎨 **Design and Content**
- **Color Palette Selection**: AI helped validate color choices for accessibility
- **Recipe Content**: Generated diverse recipe examples for testing and demonstrations
- **Code Organization**: Structured CSS into logical, maintainable sections
- **Error Handling**: Implemented comprehensive error handling patterns

### ⚖️ **Maintaining Human Oversight**
- **Code Review**: All AI-generated code was manually reviewed and tested
- **Business Logic**: Critical application logic was human-designed and validated
- **User Experience**: UX decisions were made based on human judgment and testing
- **Security**: Security implementations were manually verified and tested

---

## Testing

### Manual Testing

#### 🔐 **Authentication Testing**
| Test Case | Expected Result | Actual Result | Status |
|-----------|----------------|---------------|---------|
| User Registration | Account created, user logged in | ✅ Working | Pass |
| User Login | User authenticated, redirected to home | ✅ Working | Pass |
| User Logout | User logged out, redirected appropriately | ✅ Working | Pass |
| Invalid Login | Error message displayed | ✅ Working | Pass |
| Password Requirements | Validation enforced | ✅ Working | Pass |

#### 📝 **Recipe Management Testing**
| Test Case | Expected Result | Actual Result | Status |
|-----------|----------------|---------------|---------|
| Create Recipe | Recipe saved to database | ✅ Working | Pass |
| Edit Own Recipe | Recipe updated successfully | ✅ Working | Pass |
| Delete Own Recipe | Recipe removed from database | ✅ Working | Pass |
| View Recipe Detail | All recipe information displayed | ✅ Working | Pass |
| Recipe List View | All recipes displayed with pagination | ✅ Working | Pass |
| Form Validation | Required fields enforced | ✅ Working | Pass |

#### 💬 **Comment System Testing**
| Test Case | Expected Result | Actual Result | Status |
|-----------|----------------|---------------|---------|
| Add Comment (Logged In) | Comment saved and displayed | ✅ Working | Pass |
| Add Comment (Not Logged In) | Redirect to login page | ✅ Working | Pass |
| Edit Own Comment | Comment updated inline | ✅ Working | Pass |
| Delete Own Comment | Comment removed from display | ✅ Working | Pass |
| Comment Moderation | New comments require approval | ✅ Working | Pass |
| Edit Comment Permissions | Only author can edit | ✅ Working | Pass |

#### 📱 **Responsive Design Testing**
| Device Type | Screen Size | Layout | Navigation | Status |
|-------------|------------|---------|------------|---------|
| Mobile | 320px-768px | ✅ Responsive | ✅ Hamburger menu | Pass |
| Tablet | 768px-1024px | ✅ Responsive | ✅ Full navigation | Pass |
| Desktop | 1024px+ | ✅ Responsive | ✅ Full navigation | Pass |
| Large Desktop | 1440px+ | ✅ Responsive | ✅ Full navigation | Pass |

#### 🎨 **UI/UX Testing**
| Feature | Expected Behavior | Actual Behavior | Status |
|---------|------------------|-----------------|---------|
| Toast Notifications | Display success/error messages | ✅ Working | Pass |
| Loading States | Show during form submissions | ✅ Working | Pass |
| Form Validation | Real-time validation feedback | ✅ Working | Pass |
| Button Hover Effects | Smooth transitions | ✅ Working | Pass |
| Modal Confirmations | Confirm destructive actions | ✅ Working | Pass |

### Automated Testing

#### 🧪 **Django Unit Tests**
```python
# Example test coverage areas:
- Model validation and methods
- View permissions and responses  
- Form validation and processing
- URL routing and resolution
- Authentication workflows
```

**Test Coverage Areas:**
- **Models**: Recipe and Comment model validation
- **Views**: All CRUD operations and permissions
- **Forms**: Form validation and error handling
- **URLs**: Route resolution and parameter passing
- **Authentication**: Login/logout workflows

#### 🔄 **Integration Testing**
- **User workflows**: Complete user journeys from registration to recipe creation
- **Comment system**: Full comment lifecycle testing
- **Permission testing**: Ensure proper access controls
- **Database integrity**: Test data consistency and relationships

### Code Validation

#### ✅ **HTML Validation**
- **W3C HTML Validator**: All templates pass validation
- **Semantic HTML**: Proper use of semantic elements
- **Accessibility**: ARIA labels and proper heading structure
- **Form validation**: Proper form structure and labels

#### ✅ **CSS Validation**
- **W3C CSS Validator**: All styles pass validation
- **CSS Organization**: Logical structure and consistent naming
- **Responsive Design**: Proper media query implementation
- **Browser Compatibility**: Cross-browser testing completed

#### ✅ **JavaScript Validation**
- **ESLint**: Code quality and consistency checks
- **Browser Compatibility**: ES6+ features with fallbacks
- **Error Handling**: Proper try-catch implementation
- **Performance**: Optimized DOM manipulation

#### ✅ **Python Code Quality**
- **PEP 8 Compliance**: Python style guide adherence
- **Django Best Practices**: Proper view and model patterns
- **Security**: Input validation and CSRF protection
- **Performance**: Optimized database queries

#### 📊 **Performance Metrics**
- **Performance**: 90+ (Optimized images and CSS)
- **Accessibility**: 95+ (Proper contrast ratios and ARIA labels)
- **Best Practices**: 100 (Security headers and HTTPS)
- **SEO**: 90+ (Meta tags and semantic structure)

#### 🔍 **Accessibility Testing**
- **Color Contrast**: All text meets WCAG AA standards
- **Keyboard Navigation**: Full site navigable via keyboard
- **Screen Reader**: Semantic HTML and ARIA labels
- **Focus Indicators**: Clear focus states for all interactive elements

#### ⚡ **Performance Optimization**
- **Image Optimization**: Compressed images and proper formats
- **CSS Minification**: Organized and efficient stylesheets
- **JavaScript Optimization**: Minimal JavaScript with efficient DOM queries
- **Caching**: Proper cache headers for static assets

---

## Deployment

### 🚀 **Local Development Setup**

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/cookbookr.git
cd cookbookr
```

2. **Create Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Database Setup**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5. **Load Sample Data**
```bash
python manage.py loaddata Recipes/fixtures/users.json
python manage.py loaddata Recipes/fixtures/recipes.json
```

6. **Run Development Server**
```bash
python manage.py runserver
```

### 🌐 **Production Deployment (Heroku)**

1. **Prepare for Deployment**
```bash
# Install production dependencies
pip install gunicorn whitenoise
pip freeze > requirements.txt

# Create Procfile
echo "web: gunicorn config.wsgi" > Procfile
```

2. **Environment Variables**
```bash
# Set in Heroku Config Vars
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-app.herokuapp.com
```

3. **Deploy to Heroku**
```bash
heroku create cookbookr-app
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### ⚙️ **Environment Configuration**

**Development Settings:**
- SQLite database for local development
- Debug mode enabled
- Django Debug Toolbar for development insights
- Local static file serving

**Production Settings:**
- PostgreSQL database
- Debug mode disabled
- WhiteNoise for static file serving
- Security middleware enabled
- Environment variable configuration

---

## Credits and Acknowledgements

### Content

#### 📚 **Educational Resources**
- **Django Documentation**: Official Django tutorials and best practices
- **Bootstrap Documentation**: Component usage and customization
- **MDN Web Docs**: HTML, CSS, and JavaScript reference materials
- **Real Python**: Django development tutorials and patterns

#### 🧑‍🏫 **Learning Support**
- **Code Institute**: Full Stack Software Development course materials
- **Django Girls Tutorial**: Foundation Django concepts and deployment
- **Python Crash Course**: Django web development chapters
- **Two Scoops of Django**: Advanced Django patterns and best practices

#### 🍳 **Recipe Content**
- **Recipe Database**: Sample recipes created for demonstration purposes
- **Food Network**: Inspiration for recipe formatting and presentation
- **AllRecipes**: Community features and user interaction patterns
- **BBC Good Food**: Recipe structure and ingredient list formatting

### Media

#### 🎨 **Design Resources**
- **FontAwesome**: Icon library for consistent UI elements
- **Bootstrap Icons**: Additional icon resources
- **Google Fonts**: Typography research and selection
- **Color Hunt**: Color palette inspiration and accessibility testing

#### 🖼️ **Images and Graphics**
- **Unsplash**: Food photography inspiration (placeholder images)
- **Pixabay**: Free stock images for design mockups
- **Hero Patterns**: CSS pattern generators for backgrounds
- **CSS Gradient**: Gradient generation tools for hero sections

#### 🛠️ **Development Tools**
- **VS Code**: Primary development environment
- **GitHub**: Version control and project hosting
- **Chrome DevTools**: Frontend debugging and optimization
- **Lighthouse**: Performance and accessibility auditing

### 🙏 **Special Thanks**

#### 👨‍💻 **Technical Support**
- **GitHub Copilot**: AI coding assistance and productivity enhancement
- **Stack Overflow Community**: Problem-solving and best practices
- **Django Community**: Framework development and maintenance
- **Bootstrap Team**: CSS framework development

#### 🎓 **Educational Mentorship**
- **Code Institute Mentors**: Project guidance and code review
- **Slack Community**: Peer support and collaborative learning
- **YouTube Django Tutorials**: Supplementary learning resources
- **Developer Twitter**: Industry insights and best practices

#### 🧪 **Testing and Feedback**
- **Family and Friends**: User testing and feedback
- **Code Institute Peers**: Code review and suggestions
- **Accessibility Testing Tools**: WAVE, axe DevTools
- **Cross-browser Testing**: BrowserStack for compatibility testing

### 📄 **License and Legal**

This project is developed for educational purposes as part of the Code Institute Full Stack Software Development course. All code is original work with appropriate attribution to learning resources and third-party libraries used.

**Third-party Libraries:**
- Django (BSD License)
- Bootstrap (MIT License)  
- FontAwesome (CC BY 4.0 License)
- jQuery (MIT License)

---

*This project represents the culmination of Full Stack Web Development learning, demonstrating proficiency in Django, database design, responsive web development, and modern software engineering practices.*